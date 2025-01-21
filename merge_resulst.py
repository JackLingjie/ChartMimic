import os  
import json  
import re  
import csv  
# 项目路径  
project_path="/home/v-lingjiang/project/ChartMimic"
  
def get_code_passed_files(modelagent):  
    template_type = modelagent.split("_")[-1].split("Agent")[0].lower()  
    file_dir = os.path.join(project_path, "results", "direct", f"chart2code_{modelagent}_results", f"{template_type}_checker")  
      
    if not os.path.exists(file_dir):  
        print(f"Directory not found: {file_dir}")  
        return []  
      
    filter_files = [item.split(".pdf")[0] + ".py" for item in os.listdir(file_dir) if ".pdf" in item]  
    return filter_files  
  
def extract_scores(response_text):  
    scores = {  
        "chart_types_score": 0,  
        "layout_score": 0,  
        "text_content_score": 0,  
        "data_score": 0,  
        "style_score": 0,  
        "clarity_score": 0,  
        "gpt4v_score": 0.0  
    }  
    patterns = {  
        "chart_types_score": r"Chart Types:.*?Score: (\d+)\/20",  
        "layout_score": r"Layout:.*?Score: (\d+)\/10",  
        "text_content_score": r"Text Content:.*?Score: (\d+)\/20",  
        "data_score": r"Data:.*?Score: (\d+)\/20",  
        "style_score": r"Style:.*?Score: (\d+)\/20",  
        "clarity_score": r"Clarity:.*?Score: (\d+)\/10",  
        "gpt4v_score": r"(?:S|s)core: (\d+)\/100"  
    }  
    for key, pattern in patterns.items():  
        match = re.search(pattern, response_text, re.IGNORECASE if key == "gpt4v_score" else 0)  
        if match:  
            scores[key] = int(match.group(1)) / (100 if key == "gpt4v_score" else 1)  
    return scores  

def process_jsonl_file(input_file):  
    data = []  
      
    with open(input_file, 'r', encoding='utf-8') as infile:  
        for line in infile:  
            entry = json.loads(line)  
            response = entry.get("response", "")  
            scores = extract_scores(response)  
            entry.update(scores)  
            data.append(entry)  
  
    with open(input_file, 'w', encoding='utf-8') as outfile:  
        for entry in data:  
            outfile.write(json.dumps(entry, ensure_ascii=False) + '\n')  

def process_model_results(model):  
    agents = ["DirectAgent"]  
    model_agent = f"{model}_DirectAgent"  
    results = {}  
  
    # 处理第一个文件集  
    filename = os.path.join(project_path, "results", "direct", f"chart2code_{model_agent}_results_code4evaluation.json")  
    if not os.path.exists(filename):  
        print(f"File not found: {filename}")  
        return results  
      
    with open(filename, 'r') as f:  
        data = [json.loads(line) for line in f]  
      
    filter_files = get_code_passed_files(model_agent)  
    data = [d for d in data if d["orginial"].split("/")[-1] in filter_files]  
      
    denominator = 500  
    results["example_count"] = len(data)  
    results["ExecRate"] = len(filter_files) / denominator * 100  
      
    # 计算各类分数  
    f1s = []  
    text_metrics = sum(d["text_metrics"]["f1"] for d in data) * 100 / denominator  
    layout_metrics = sum(d["layout_metrics"]["f1"] for d in data) * 100 / denominator  
    chart_type_metrics = sum(d["chart_type_metrics"]["f1"] for d in data) * 100 / denominator  
    color_metrics = sum(d["color_metrics"]["f1"] for d in data) * 100 / denominator  
      
    f1s.extend([text_metrics, layout_metrics, chart_type_metrics, color_metrics])  
      
    results["TextScore"] = text_metrics  
    results["LayoutScore"] = layout_metrics  
    results["TypeScore"] = chart_type_metrics  
    results["ColorScore"] = color_metrics  
    results["Average"] = sum(f1s) / len(f1s)  
  
    # 处理第二个文件集  
    file = os.path.join(project_path, "results", f"gpt4evaluation_{model}_GPT4EvaluationAgent_direct_results.json")  
    
    # extract gpt4v score
    process_jsonl_file(file)
    if not os.path.exists(file):  
        print(f"File not found: {file}")  
        results["GPT4VScore"] = 0  
        results["Overall"] = 0  
        return results 
      
    with open(file, 'r') as f:  
        data = [json.loads(line) for line in f]  
      
    filter_files_pdf = [item.replace(".py", ".pdf") for item in filter_files]  
    data = [d for d in data if d["orginial"].split("/")[-1] in filter_files_pdf]  
      
    try:
        if len(data) > 0:  
            gpt4v_score = sum(d["gpt4v_score"] for d in data) * 100 / denominator  
            results["GPT4VScore"] = gpt4v_score  
        else:  
            results["GPT4VScore"] = None  
    except KeyError as e:
        print(f"KeyError: {e} in model: {model}")  
        results["GPT4VScore"] = 0
    # 计算总体分数  
    results["Overall"] = sum([results.get("Average", 0), results.get("GPT4VScore", 0)]) / 2  
  
    return results  
  
# # 对每个模型调用函数并存储结果  
# models = [  
#     "Llama-3.2-11B-Vision-Instruct",  
#     'gpt-4o',  
#     'llava-onevision-qwen2-7b-ov-hf',  
#     'Qwen2-VL-7B-Instruct',  
#     'gpt-4o-mini',  
#     'qwen2vl',  
#     'MiniCPM-V-2_6'  
# ]  
# 模型和代理配置  
def extract_models():  
    # 获取目录路径  
    directory_path = os.path.join(project_path, "results/direct")  
      
    # 列出目录中的所有文件夹  
    all_entries = os.listdir(directory_path)  
      
    # 使用正则表达式提取模型名  
    model_pattern = re.compile(r'chart2code_(.*?)_DirectAgent_results')  
    models = []  
      
    for entry in all_entries:  
        entry_path = os.path.join(directory_path, entry)  
        # 检查是否为目录  
        if os.path.isdir(entry_path):  
            match = model_pattern.match(entry)  
            if match:  
                models.append(match.group(1))  
      
    return models

# 对每个模型调用函数并存储结果  
models = extract_models()  
# models = ["Qwen2-VL-7B-Instruct"]
final_results = {model: process_model_results(model) for model in models}  
  
# 对结果按 Overall 分数降序排序  
sorted_final_results = dict(sorted(final_results.items(), key=lambda item: item[1].get('Overall', 0), reverse=True))  
  
# 定义输出 CSV 文件的路径  
output_csv_file = 'results_chartmimic.csv'  
  
# 提取所有字段名（假设所有模型有相同的字段）  
fieldnames = ['model_name', 'Overall', 'GPT4VScore', "Average"] + [key for key in next(iter(final_results.values())).keys() if key not in ['Overall', 'GPT4VScore', "Average"]]  
  
# 写入 CSV 文件  
with open(output_csv_file, 'w', newline='') as csvfile:  
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  
  
    # 写入头  
    writer.writeheader()  
  
    # 写入每个模型的数据  
    for model_name, scores in sorted_final_results.items():  
        row = {'model_name': model_name}  
        row.update(scores)  
        writer.writerow(row)  
  
print(f"Results have been written to {output_csv_file}")  