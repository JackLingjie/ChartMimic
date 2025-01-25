import json  
import os  
from concurrent.futures import ThreadPoolExecutor, as_completed  
from tqdm import tqdm  
from gpt4o import Openai, API_INFOS  
import re  
  
# Define the prompt template  

  
MACHINE_ID = 2  
def load_data(file_path):  
    try:  
        with open(file_path, 'r') as f:  
            return json.load(f)  
    except Exception as e:  
        print(f"Error loading data from {file_path}: {e}")  
        return []  
  
def get_revised_text(client, prompt_template, image_path, max_tokens=2048):  
    content = prompt_template
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
    match = re.search(r"```html(.*?)```", gpt_answer, re.DOTALL)  
    return match.group(1).strip() if match else ""  
  
def process_row(index, client, item, max_tokens=2048):  
    # code = item.get('revised_text', '').strip()  
    # category = item.get('category', 'pie')  
    image_path = item.get('images', [0])[0]
    prompt = item.get('gpt_prompt', '')
    # image_path = item["images"]
    # print(f"image_path: {image_path}")
    if not image_path:  
        print(f"No image path found for index {index}. Skipping.")  
        return None  
  
    evol_text, gpt_answer, stop_reason = get_revised_text(  
        client, prompt, image_path, max_tokens  
    )  
  
    result = {  
        'index': index,  
        'code_extract': evol_text,  
        'generate_raw': gpt_answer,  
        'stop_reason': stop_reason,
        "model": "gpt4o"
    }  
  
    result.update(item)  
    return result  
  
def main():  
    # save_path = "/mnt/lingjiejiang/multimodal_code/data/chart_data/evol_data_filter_images_40k_sharegpt_format.json"   
    save_path = f"/mnt/lingjiejiang/multimodal_code/data/dpo/html/web100k_split{MACHINE_ID}.json"  
    output_dir = f'/mnt/lingjiejiang/multimodal_code/data/dpo/html/generate{MACHINE_ID}'  
    # output_dir = "tests/"
    print(f"save_path: {save_path}")
    print(f"output_dir: {output_dir}")
    os.makedirs(output_dir, exist_ok=True)  
  
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
                process_row, i, clients[i % len(clients)], item, max_tokens  
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