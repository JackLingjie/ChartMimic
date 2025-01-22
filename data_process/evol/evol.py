import json  
import os  
from concurrent.futures import ThreadPoolExecutor, as_completed  
# import logging  
from tqdm import tqdm  
from gpt4o import Openai, API_INFOS  
import re  

# 配置日志记录  
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')  
# 下面这个是我对图表代码进行优化的prompt，帮我对这个prompt进行修改完善，使其能让gpt更好的生成图表，给出修改后的英语prompt
prompt_template = \
"""  
As a Matplotlib expert, your task is to optimize a Python plotting script to create a visually complex and appealing chart. The script will be used for a Matplotlib chart demonstration, so aesthetic quality is essential. You are required to generate a {type} chart, tailoring all modifications to enhance this specific chart type.  
  
If the original code is not optimal, make necessary adjustments to improve its performance and visual appeal. Enhance the chart by adding or modifying elements such as colors, markers, and line styles, ensuring each addition is meaningful and contributes to the chart's clarity and impact.  
  
Based on the specified chart type and initial script, enrich the chart's narrative through elements like the title, axis labels, and legend.  
  
Use the Matplotlib library in Python for plotting. You can use auxiliary libraries such as Numpy, but make sure the code works! Avoid using seaborn or other plot library.

Instead of using the original data, construct new, contextually appropriate data that aligns with a formal chart scenario. Use Python lists or NumPy arrays to create this data, ensuring it is explicitly crafted to suit the chart type and topic. Avoid using random() for data creation.  
  
Be imaginative and creative in both data selection and plotting details to produce an engaging and informative chart.  
  
Please provide the optimized code within a ```python``` block: 
  
<Original Code>
{RAW_CODE}
<Original Code> 

""" 

MACHINE_ID = 1
# Read JSON data  
def load_data(file_path):  
    try:  
        with open(file_path, 'r') as f:  
            return json.load(f)  
    except Exception as e:  
        print(f"Error loading data from {file_path}: {e}")  
        return []  
  
# Call GPT API and parse response  
def get_revised_text(client, instruction, category, prompt_template, max_tokens=2048):  
    content = prompt_template.format(RAW_CODE=instruction, type=category)
    with open("debug.txt", "w") as f:
        f.write(content)  
    try:  
        gpt_answer = client.get_response(content=content, max_tokens=max_tokens)  
    except Exception as e:  
        print(f"Error calling GPT API: {e}")  
        return "", ""  
  
    if not gpt_answer:  
        return "", ""  
  
    evol_text = extract_python_code(gpt_answer)  
  
    return evol_text, gpt_answer  
  
def extract_python_code(gpt_answer):  
    # Use regex to find the code block marked with ```python  
    match = re.search(r"```python(.*?)```", gpt_answer, re.DOTALL)  
    return match.group(1).strip() if match else ""  
  
# Process a single row of data  
def process_row(index, client, row, prompt_template, max_tokens=2048):  
    code = row.get('revised_text', '').strip()  
    category = row.get('category', 'pie')  
    evol_text, gpt_answer = get_revised_text(  
        client, code, category, prompt_template, max_tokens=max_tokens  
    )  
  
    result = {  
        'index': index,  
        'evol_text': evol_text,  
        'gpt_evol_answer': gpt_answer  
    }  
  
    result.update(row)  
    return result  
  
def main():  
    save_path = f"/mnt/lingjiejiang/multimodal_code/data/chart_data/direct_revised_39k_split_{MACHINE_ID}.json"  
    output_dir = f'/mnt/lingjiejiang/multimodal_code/data/chart_data/chart_code_evol_{MACHINE_ID}'  
    os.makedirs(output_dir, exist_ok=True)  
  
    data = load_data(save_path)  
    data = data[:5]  # 这里限制为前 5 条，您可以根据需要调整  
  
    clients = [Openai(apis=[API_INFOS[i]]) for i in range(len(API_INFOS))]  
    print(f"len(clients): {len(clients)}")  
    max_tokens = 2048  
    batch_size = 1000  
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
                    json.dump(revised_data, f, indent=2)  # 写入 JSON 格式  
  
    # 保存最终结果  
    final_file = os.path.join(output_dir, "final_output.json")  
    with open(final_file, 'w') as f:  
        json.dump(revised_data, f, indent=2)  # 写入 JSON 格式  
  
if __name__ == "__main__":  
    main()  