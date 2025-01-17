import os  
import json  
import pandas as pd  
# from llm import load_llm  
# chart2code/data/data_utils
from chart2code.data.data_utils import Chart2CodeDataset
# from utils.logging.agent_logger import AgentLogger  
  
# # Logger setup  
# logger = AgentLogger(__name__)  
  
# 加载数据集  
def load_dataset(dataset_name, dataset_dir, direct_dir=None):  
    if dataset_name == "chart2code":  
        dataset = Chart2CodeDataset(dataset_dir=dataset_dir, direct_dir=direct_dir)  
    else:  
        raise NotImplementedError(f"Dataset {dataset_name} not implemented")  
    return dataset  
  
# 构造提示  
def construct_prompt(file, dimensions_info, instruction):  
    width, height = get_pdf_dimensions(file, dimensions_info)  
    prompt = {  
        "role": "user",  
        "content": [  
            {  
                "type": "text",  
                "text": instruction.format(height=height, width=width),  
            },  
            {"type": "image", "image_url": file.replace(".pdf", ".png")},  
        ],  
    }  
    return [prompt]  
  
# 获取 PDF 尺寸  
def get_pdf_dimensions(pdf_path, dimensions_info):  
    file_idx = "{}_{}".format(  
        pdf_path.split("/")[-1].split("_")[0],  
        pdf_path.split("/")[-1].split("_")[1],  
    ).replace(".pdf", "")  
    width = dimensions_info[dimensions_info["idx"] == file_idx]["width"].values[0]  
    height = dimensions_info[dimensions_info["idx"] == file_idx]["height"].values[0]  
    return width, height  
  
# 生成内容  
def generate_content(llm, conversation):  
    response = llm.generate(conversation)  
    return response  
  
# 保存结果  
def save_results(results, results_file):  
    with open(results_file, "w", encoding="utf-8") as f:  
        for result in results:  
            json_str = json.dumps(result)  
            f.write(json_str + "\n")  
  
# 主函数  
def main():  
    # 配置参数  
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
      
    # 加载 LLM 和提示  
    # llm = load_llm(llm_config["name"], llm_config)  
    llm = None
    prompt_data = json.load(open(agent_config["prompt_path"], "r"))  
    instruction = prompt_data["instruction"]  
      
    # 加载数据集  
    dataset = load_dataset(run_config["name"], run_config["dataset_dir"])  
  
    # 加载尺寸信息  
    dimensions_info = pd.read_json(  
        f"dimentions_info.jsonl",  
        lines=True,  
    )  
      
    # 处理数据集并生成内容  
    results = []  
    print(f"Processing {len(dataset)} files")
    for data in dataset:  
        file = data["file"]  
        conversation = construct_prompt(file, dimensions_info, instruction)  
        response = generate_content(llm, conversation)  
        results.append({"file": file, "response": response})  
  
    # 保存结果  
    os.makedirs(run_config["result_dir"], exist_ok=True)  
    results_file = os.path.join(run_config["result_dir"], "results.json")  
    save_results(results, results_file)  
  
# 执行主函数  
if __name__ == "__main__":  
    main()  