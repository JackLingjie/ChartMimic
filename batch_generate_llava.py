import os  
import json  
import pandas as pd  
from chart2code.data.data_utils import Chart2CodeDataset  
import base64
from io import BytesIO
from PIL import Image
from vllm_models.vllm_qwen import VllmModel
import argparse

def encode_image(image_path):
	with open(image_path, "rb") as image_file:
		return base64.b64encode(image_file.read()).decode('utf-8')
     
def load_dataset(dataset_name, dataset_dir, direct_dir=None):  
    if dataset_name == "chart2code":  
        dataset = Chart2CodeDataset(dataset_dir=dataset_dir, direct_dir=direct_dir)  
    else:  
        raise NotImplementedError(f"Dataset {dataset_name} not implemented")  
    return dataset  
  
def construct_prompt(file, dimensions_info, instruction):  
    width, height = get_pdf_dimensions(file, dimensions_info)  
    # img = Image.open(file.replace(".pdf", ".png"))
    img = file.replace(".pdf", ".png")
    prompt = instruction.format(height=height, width=width)

    messages = [  
            {  
                "role": "user",  
                "content": f"<image>\n{prompt}"
            }  
    ]  
  
    return (messages, img) 
  
def get_pdf_dimensions(pdf_path, dimensions_info):  
    file_idx = "{}_{}".format(  
        pdf_path.split("/")[-1].split("_")[0],  
        pdf_path.split("/")[-1].split("_")[1],  
    ).replace(".pdf", "")  
    width = dimensions_info[dimensions_info["idx"] == file_idx]["width"].values[0]  
    height = dimensions_info[dimensions_info["idx"] == file_idx]["height"].values[0]  
    return width, height  
  
def save_results(results, results_file):  
    with open(results_file, "w", encoding="utf-8") as f:  
        for result in results:  
            json_str = json.dumps(result)  
            f.write(json_str + "\n")  
  
def main():  
    parser = argparse.ArgumentParser(description="Process some models.")  
    parser.add_argument('--model_name', type=str, default="/mnt/lingjiejiang/textual_aesthetics/model_checkpoint/vlm_checkpoints/Qwen2-VL-7B-Instruct" , help='The name of the model to use')  
    parser.add_argument('--model_path', type=str, default="Qwen2-VL-7B-Instruct", help='The path to the model checkpoint')  
  
    args = parser.parse_args()  

    run_config = {  
        "result_dir": "results/direct",  
        "name": "chart2code",  
        "dataset_dir": "dataset/ori_500"  
    }  
      
    llm_config = {  
        "name": "gpt",  
        "engine": "gpt-4o",  
        "context_length": 4096,  
        "max_tokens": 4096,  
        "temperature": 0.0,  
        "top_p": 1,  
        "retry_delays": 20,  
        "max_retry_iters": 15,  
        "stop": []  
    }  
      
    agent_config = {  
        "prompt_path": "chart2code/prompts/DirectAgent/gpt-4-vision-preview.json"  
    }  
    model_name = args.model_name
    # Load LLM and prompt  
    if model_name == "MiniCPM-V-2_6":
         from vllm_models.vllm_cpm import VllmModel
    elif model_name == "Llama-3.2-11B-Vision-Instruct":
        from vllm_models.vllm_llama import VllmModel
    elif model_name == "llava-onevision-qwen2-7b-ov-hf":
        from vllm_models.vllm_llava import VllmModel
        
    llm = VllmModel(args.model_path)  
    # llm = None
    prompt_data = json.load(open(agent_config["prompt_path"], "r"))  
    instruction = prompt_data["instruction"]  
      
    # Load dataset  
    dataset = load_dataset(run_config["name"], run_config["dataset_dir"])  
      
    # Load dimensions info  
    dimensions_info = pd.read_json("dimentions_info.jsonl", lines=True)  
      
    # Process dataset and generate content  
    results = []  
    print(f"Processing {len(dataset)} files")  
      
    # Batch processing  
    batch_size = 32  
    dataset = dataset
    for i in range(0, len(dataset), batch_size):  
        batch_data = dataset[i:i + batch_size]  
        batch_prompts = []  
        batch_files = []  
          
        for data in batch_data:  
            file = data["file"]  
            batch_files.append(file)  
            conversation_img = construct_prompt(file, dimensions_info, instruction)  
            batch_prompts.append(conversation_img)  
        messages_list = [item[0] for item in batch_prompts]
        image_list = [item[1] for item in batch_prompts]
        responses = llm.batch_generate(messages=messages_list, image_sources=image_list, temperature=llm_config["temperature"], max_tokens=llm_config["max_tokens"])  
          
        for file, response in zip(batch_files, responses):  
            results.append({"file": file, "response": response})  
      
    # Save results  
    os.makedirs(run_config["result_dir"], exist_ok=True)
    results_file = os.path.join(run_config["result_dir"], "results_test.json")  
    
    results_file = f"results/direct/chart2code_{model_name}_DirectAgent_results.json"
    save_results(results, results_file)  
  
if __name__ == "__main__":  
    main()  