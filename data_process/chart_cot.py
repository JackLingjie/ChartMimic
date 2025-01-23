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
I need your assistance in generating Python code using matplotlib that can accurately reproduce the provided image. Please ensure the following:  

1. Before generating the code, analyze the chart elements such as text, labels, datas, chart type, layout, and colors. Provide a brief explanation of your thought process for each element.  
 
2. After the analysis, provide the complete matplotlib code. Use `figsize=({width}, {height})` to set the image size so that it matches the original dimensions. Present the final code within a ```python``` block.
""" 

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
    save_path = "/mnt/lingjiejiang/multimodal_code/data/chart_data/sampled_seed_4k.json"
    output_dir = '/mnt/lingjiejiang/multimodal_code/data/chart_data/chart_code_evol_sampled_seed_4k_supply'  
    # output_dir = "data_process/tests"
    os.makedirs(output_dir, exist_ok=True)  
  
    data = load_data(save_path)  
    # data = data[:2]
    output_dir = "data_process/tests"
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
                intermediate_file = os.path.join(output_dir, f"intermediate_batch_empty_{batch_number}.json")  
                with open(intermediate_file, 'w') as f:  
                    json.dump(revised_data, f, indent=0)  # Write list to JSON format  
  
    # Save the final result  
    final_file = os.path.join(output_dir, "final_output_empty.json")  
    with open(final_file, 'w') as f:  
        json.dump(revised_data, f, indent=2)  # Write list to JSON format  
  
if __name__ == "__main__":  
    main() 