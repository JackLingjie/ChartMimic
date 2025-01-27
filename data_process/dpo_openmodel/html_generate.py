import json
import os
import argparse
from tqdm import tqdm
import base64
from PIL import Image
import re
from vllm_qwen import VllmModel

MACHINE_ID = 1

def load_data(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        return []

def construct_prompt(image_path, instruction):
    img = Image.open(image_path)
    prompt = instruction
    
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "image": img,
                    "min_pixels": 224 * 224,
                    "max_pixels": 2560 * 1440,
                },
                {
                    "type": "text", 
                    "text": prompt
                }
            ],
        }
    ]
    return messages

def extract_code(gpt_answer):
    match = re.search(r"```html(.*?)```", gpt_answer, re.DOTALL)
    if match:
        return match.group(1).strip()
    
    match = re.search(r"```python(.*?)```", gpt_answer, re.DOTALL)
    if match:
        return match.group(1).strip()
    
    return ""

def batch_generate(client, prompts, max_tokens=2048):
    try:
        responses, stop_reasons = client.batch_generate(prompts, max_tokens=max_tokens)
    except Exception as e:
        print(f"Error during batch inference: {e}")
        return [], []
    return responses, stop_reasons

def process_batch(client, batch_data, max_tokens=2048, model_name="qwen"):
    batch_prompts = []
    
    for item in batch_data:
        image_path = item.get('images', [0])[0]
        prompt = item.get('gpt_prompt', '')
        
        if not image_path:
            print(f"No image path found for index {item.get('index')}. Skipping.")
            continue
        
        prompt_message = construct_prompt(image_path, prompt)
        batch_prompts.append(prompt_message)
    
    responses, stop_reasons = batch_generate(client, batch_prompts, max_tokens)
    
    results = []
    for idx, (response, stop_reason) in enumerate(zip(responses, stop_reasons)):
        evol_text = extract_code(response)
        
        item = batch_data[idx]
        item['code_extract'] = evol_text
        item['generate_raw'] = response
        item['stop_reason'] = stop_reason
        item["model"] = model_name

        results.append(item)
    
    return results

def main():
    parser = argparse.ArgumentParser(description="Process some models.")
    parser.add_argument('--model_name', type=str, default="Qwen2-VL-7B-Instruct", help='The name of the model to use')
    parser.add_argument('--model_path', type=str, default="/mnt/lingjiejiang/textual_aesthetics/model_checkpoint/vlm_checkpoints/Qwen2-VL-7B-Instruct", help='The path to the model checkpoint')
    parser.add_argument('--start_index', type=int, default=0, help='Start index for processing')
    parser.add_argument('--end_index', type=int, default=-1, help='End index for processing')
    
    args = parser.parse_args()
    
    model_name = args.model_name
    model_path = args.model_path
    start_index = args.start_index
    end_index = args.end_index

    save_path = "/mnt/lingjiejiang/multimodal_code/data/dpo/merged_html_chart_150k.json"
    output_dir = f'/mnt/lingjiejiang/multimodal_code/data/dpo/{model_name}_generate'
    os.makedirs(output_dir, exist_ok=True)
    
    data = load_data(save_path)
    
    if end_index == -1 or end_index > len(data):
        end_index = len(data)

    print(f"Processing data from index {start_index} to {end_index}")
    data = data[start_index:end_index]

    client = VllmModel(model_path=model_path)
    print(f"Using model: {model_name}")
    
    batch_size = 4
    revised_data = []
    for i in tqdm(range(0, len(data), batch_size), desc=f"Processing Batches {start_index}:{end_index}", unit="batch"):
        batch_data = data[i:i + batch_size]
        
        batch_results = process_batch(client, batch_data, model_name=model_name)
        revised_data.extend(batch_results)

        if (i // batch_size) % 100 == 0 and i > 0:
            print(f"[INFO] Processed {i} batches (~{i * batch_size} items)...")

    output_file = os.path.join(output_dir, f"output_{start_index}_{end_index}.json")
    with open(output_file, 'w') as f:
        json.dump(revised_data, f, indent=2)
    
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    main()
