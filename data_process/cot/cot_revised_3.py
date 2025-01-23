import json  
import os  
from concurrent.futures import ThreadPoolExecutor, as_completed  
from tqdm import tqdm  
from gpt4o import Openai, API_INFOS  
import re  
  
# Define the prompt template  
prompt_template = \
"""  
I need your assistance in generating Python code using matplotlib that can accurately reproduce the provided image. Please ensure the following:  
1. Before generating the code, analyze the chart elements such as text, labels, datas, chart type, layout, and colors. Provide a brief explanation of your thought process for each element.  
2. After the analysis, provide the complete matplotlib code. Use `figsize=({width}, {height})` to set the image size so that it matches the original dimensions. Present the final code within a ```python``` block.
""" 
  
MACHINE_ID = 3  
def load_data(file_path):  
    try:  
        with open(file_path, 'r') as f:  
            return json.load(f)  
    except Exception as e:  
        print(f"Error loading data from {file_path}: {e}")  
        return []  
  
def get_revised_text(client, prompt_template, image_path, width, height, max_tokens=2048):  
    content = prompt_template.format(width=width, height=height)  
    # with open("debug.txt", "w") as f:  
    #     f.write(content)  
  
    try:  
        gpt_answer, stop_reason = client.get_image_response_v2_raw(  
            content=content, image=image_path, max_tokens=max_tokens  
        )  
    except Exception as e:  
        print(f"Error calling GPT API: {e}")  
        return "", "", ""  
  
    if not gpt_answer:  
        return "", "", ""  
  
    evol_text = extract_python_code(gpt_answer)  
    return evol_text, gpt_answer, stop_reason  
  
def extract_python_code(gpt_answer):  
    match = re.search(r"```python(.*?)```", gpt_answer, re.DOTALL)  
    return match.group(1).strip() if match else ""  
  
def process_row(index, client, item, prompt_template, max_tokens=2048):  
    # code = item.get('revised_text', '').strip()  
    # category = item.get('category', 'pie')  
    image_path = item.get('images', [])[0]
    # image_path = item["images"]
    # print(f"image_path: {image_path}")
    if not image_path:  
        print(f"No image path found for index {index}. Skipping.")  
        return None  
  
    chart_size = item.get('chart_size', [6.0, 4.0])  
    width, height = chart_size  
    width = int(chart_size[0]) if chart_size[0].is_integer() else chart_size[0]  
    height = int(chart_size[1]) if chart_size[1].is_integer() else chart_size[1]  

    evol_text, gpt_answer, stop_reason = get_revised_text(  
        client, prompt_template, image_path, width, height, max_tokens  
    )  
  
    result = {  
        'index': index,  
        'cot_text': evol_text,  
        'gpt_cot_answer_raw_answer': gpt_answer,  
        'stop_reason': stop_reason  
    }  
  
    result.update(item)  
    return result  
  
def main():  
    # save_path = "/mnt/lingjiejiang/multimodal_code/data/chart_data/evol_data_filter_images_40k_sharegpt_format.json"   
    save_path = f"/mnt/lingjiejiang/multimodal_code/data/chart_data/evol_data_filter_images_40k_split_{MACHINE_ID}.json"  
    output_dir = f'/mnt/lingjiejiang/multimodal_code/data/chart_data/chart_code_cot_{MACHINE_ID}'  
    # output_dir = "data_process/tests"
    os.makedirs(output_dir, exist_ok=True)  
    print(f"save_path: {save_path}")
    print(f"output_dir: {output_dir}")  
    data = load_data(save_path)  
    # data = data[:2]  # 这里限制为前 5 条，您可以根据需要调整
    
    clients = [Openai(apis=[API_INFOS[i]]) for i in range(len(API_INFOS))]  
    print(f"len(clients): {len(clients)}")  
    max_tokens = 2048  
    batch_size = 1000  
    revised_data = []  
  
    with ThreadPoolExecutor(max_workers=len(clients)) as executor:  
        futures = [  
            executor.submit(  
                process_row, i, clients[i % len(clients)], item, prompt_template, max_tokens  
            ) for i, item in enumerate(data)  
        ]  
  
        for i, future in enumerate(tqdm(as_completed(futures), total=len(futures))):  
            result = future.result()  
            if result:  
                revised_data.append(result)  
            if (i + 1) % batch_size == 0:  
                batch_number = (i + 1) // batch_size  
                intermediate_file = os.path.join(output_dir, f"intermediate_batch_{batch_number}.json")  
                with open(intermediate_file, 'w') as f:  
                    json.dump(revised_data, f, indent=2)  
  
    final_file = os.path.join(output_dir, "final_output.json")  
    with open(final_file, 'w') as f:  
        json.dump(revised_data, f, indent=2)  
  
if __name__ == "__main__":  
    main()  