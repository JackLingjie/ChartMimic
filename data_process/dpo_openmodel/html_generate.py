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
    # 读取图片并构造prompt
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
                    "max_pixels": 4259840,
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
    # 首先尝试提取 HTML 代码
    match = re.search(r"```html(.*?)```", gpt_answer, re.DOTALL)
    if match:
        return match.group(1).strip()
    
    # 如果没有 HTML，尝试提取 Python 代码
    match = re.search(r"```python(.*?)```", gpt_answer, re.DOTALL)
    if match:
        return match.group(1).strip()
    
    # 如果都没有提取到代码，返回空字符串
    return ""

def batch_generate(client, prompts, max_tokens=2048):
    try:
        # 批量推理
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
        
        # 构造prompt
        prompt_message = construct_prompt(image_path, prompt)
        batch_prompts.append(prompt_message)
    
    # 批量推理
    responses, stop_reasons = batch_generate(client, batch_prompts, max_tokens)
    
    # 处理批量推理结果
    results = []
    for idx, (response, stop_reason) in enumerate(zip(responses, stop_reasons)):
        # 提取evol_text（假设是HTML代码提取）
        evol_text = extract_code(response)
        
        # 更新item
        item = batch_data[idx]
        item['code_extract'] = evol_text
        item['generate_raw'] = response
        item['stop_reason'] = stop_reason
        item["model"] = model_name

        results.append(item)
    
    return results

def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="Process some models.")
    parser.add_argument('--model_name', type=str, default="Qwen2-VL-7B-Instruct", help='The name of the model to use')
    parser.add_argument('--model_path', type=str, default="/mnt/lingjiejiang/textual_aesthetics/model_checkpoint/vlm_checkpoints/Qwen2-VL-7B-Instruct", help='The path to the model checkpoint')
    args = parser.parse_args()
    
    # 获取命令行传入的模型名称
    model_name = args.model_name
    model_path = args.model_path
    
    # 定义文件路径
    # save_path = f"/mnt/lingjiejiang/multimodal_code/data/dpo/html/web100k.json"
    save_path = "/mnt/lingjiejiang/multimodal_code/data/dpo/merged_html_chart_150k.json"
    output_dir = f'/mnt/lingjiejiang/multimodal_code/data/dpo/{model_name}_generate'
    os.makedirs(output_dir, exist_ok=True)
    
    # 加载数据
    data = load_data(save_path)
    # data = data[:2]
    # output_dir = "tests/"
    # 初始化VllmModel客户端
    client = VllmModel(model_path=model_path)
    print(f"Using model: {model_name}")
    
    # 每次处理批量数据时的逻辑
    batch_size = 16
    revised_data = []
    for i in tqdm(range(0, len(data), batch_size), desc="Processing Batches", unit="batch"):
        batch_data = data[i:i + batch_size]
        
        # 批量处理
        batch_results = process_batch(client, batch_data, model_name=model_name)
        
        # 将结果更新到revised_data中
        revised_data.extend(batch_results)
        
    # 保存最终结果
    final_file = os.path.join(output_dir, "final_output.json")
    with open(final_file, 'w') as f:
        json.dump(revised_data, f, indent=2)

if __name__ == "__main__":
    main()
