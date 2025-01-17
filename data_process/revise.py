import json  
import os  
from concurrent.futures import ThreadPoolExecutor, as_completed  
# import logging  
from tqdm import tqdm  
from gpt4o import Openai, API_INFOS  
  
# 配置日志记录  
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')  
  
prompt_template = """  
Please modify the following code according to these requirements:  
1. Retain only the plotting code and necessary imports; keep only matplotlib and numpy-related libraries. Do not use os, sys, or similar libraries.  
2. Avoid using custom functions or classes. Provide sequential code for plotting. If the original code is too complex or lacks plotting code, provide a new example using matplotlib.  
3. Set the figure size to `figsize=(width, height)`.  
4. Convert all text to English; do not add font settings.  
5. If multiple plots exist, retain only one.  
6. Use `plt.show()` to display the plot.  
7. Remove non-English text, path information, and initial comments from the code. Ensure the output format matches the example.  
8. Classify the resulting plot into one of the following categories: Bar, Line, ErrorBar, Heatmap, Box, Scatters, Hist, Radar, 3D, Pie, ErrorPoint, Violin, Area, Contour, Density, Graph, Quiver, Treemap, Combination, HR, Multidiff, PIP.  
9. Output the image dimensions as `(width, height)`.   
  
Please follow the reference code format for modification:  

## Code needs to be revised:

{RAW_CODE}  
  
## Reference output format:  
  
<REVISED CODE BEGIN>  
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D  
import numpy as np  
  
# Sample data  
targets = np.array([  
    [0.2, 0.4, 0.0],  
    [0.3, 0.5, 0.2],  
    [0.4, 0.6, 0.4],  
    [0.5, 0.7, 0.6],  
    [0.6, 0.8, 0.8],  
    [0.7, 0.9, 1.0],  
    [0.8, 1.0, 1.2],  
    [0.9, 1.1, 1.4]  
])  
  
# Create a new figure  
fig = plt.figure(figsize=(7.0, 7.0))  
ax = fig.add_subplot(111, projection='3d')  
  
# Plot the targets  
ax.plot(targets[:, 0], targets[:, 1], targets[:, 2], 'o-', color='orange', label='Targets')  
  
# Set labels  
ax.set_xlabel('X')  
ax.set_ylabel('Y')  
ax.set_zlabel('Z')  
  
# Add a legend  
ax.legend()  
  
# Show the plot  
plt.show()  
<REVISED CODE END>  
  
<CATEGORY>: [Line]  
<CHART SIZE>: (7.0, 7.0)  
"""  

# 读取 JSON 数据  
def load_data(file_path):  
    try:  
        with open(file_path, 'r') as f:  
            return json.load(f)  
    except Exception as e:  
        print(f"Error loading data from {file_path}: {e}")  
        return []  
  
# 调用 GPT API 并解析响应  
def get_revised_text(client, instruction, prompt_template, max_tokens=2048):  
    content = prompt_template.format(RAW_CODE=instruction)  
    with open("debug.txt", "w") as f:
        f.write(content)
    try:  
        gpt_answer = client.get_response(content=content, max_tokens=max_tokens)  
    except Exception as e:  
        print(f"Error calling GPT API: {e}")  
        return "", "", "", ""  
  
    if not gpt_answer:  
        return "", "", "", ""  
  
    revised_text = extract_revised_text(gpt_answer)  
    category = extract_category_from_gpt_answer(gpt_answer)  
    chart_size = extract_size_from_gpt_answer(gpt_answer)  
  
    return revised_text, category, chart_size, gpt_answer  
  
def extract_revised_text(gpt_answer):  
    start = gpt_answer.find("<REVISED CODE BEGIN>") + len("<REVISED CODE BEGIN>")  
    end = gpt_answer.find("<REVISED CODE END>", start)  
    return gpt_answer[start:end].strip() if start != -1 and end != -1 else ""  
  
def extract_category_from_gpt_answer(gpt_answer):  
    start = gpt_answer.find("<CATEGORY>: [") + len("<CATEGORY>: [")  
    end = gpt_answer.find("]", start)  
    return gpt_answer[start:end].strip() if start != -1 and end != -1 else ""  
  
def extract_size_from_gpt_answer(gpt_answer):  
    start = gpt_answer.find("<CHART SIZE>: (") + len("<CHART SIZE>: (")  
    end = gpt_answer.find(")", start)  
    size_str = gpt_answer[start:end].strip() if start != -1 and end != -1 else ""  
    try:  
        width, height = map(float, size_str.split(','))  
        return (width, height)  
    except ValueError:  
        return (0.0, 0.0)  
  
# 处理单行数据  
def process_row(index, client, row, prompt_template, max_tokens=2048):  
    code = row.get('text', '').strip()  
    revised_text, category, chart_size, gpt_answer = get_revised_text(  
        client, code, prompt_template, max_tokens=max_tokens  
    )  
  
    result = {  
        'index': index,  
        'revised_text': revised_text,  
        'category': category,  
        'chart_size': chart_size,  
        'gpt_answer': gpt_answer  
    }  
  
    result.update(row)  
    return result 

def main():  
    save_path = '/mnt/lingjiejiang/multimodal_code/data/chart_data/github_chart/merged_v1_v2_3.json'  
    output_dir = '/mnt/lingjiejiang/multimodal_code/data/chart_data/revised_code'  
    os.makedirs(output_dir, exist_ok=True)  
  
    data = load_data(save_path)  
      
    # data = data[:10]
    
    clients = [Openai(apis=[API_INFOS[i]]) for i in range(len(API_INFOS))]  
    print(f"len(clients): {len(clients)}")
    max_tokens = 2048  
    batch_size = 10000  
    revised_data = []  
  
    with ThreadPoolExecutor(max_workers=len(clients)) as executor:  
        futures = [  
            executor.submit(  
                process_row, i, clients[i % len(clients)], row, prompt_template, max_tokens  
            ) for i, row in enumerate(data)  
        ]  
  
        for i, future in enumerate(tqdm(as_completed(futures), total=len(futures))):  
            revised_data.append(future.result())  
            if (i + 1) % batch_size == 0:  
                batch_number = (i + 1) // batch_size  
                intermediate_file = os.path.join(output_dir, f"intermediate_batch_{batch_number}.json")  
                with open(intermediate_file, 'w') as f:  
                    json.dump(revised_data, f, indent=0)  # 将列表写入 JSON 格式  
  
    # 最后保存完整结果  
    final_file = os.path.join(output_dir, "final_output.json")  
    with open(final_file, 'w') as f:  
        json.dump(revised_data, f, indent=0)  # 将列表写入 JSON 格式  
  
if __name__ == "__main__":  
    main()  