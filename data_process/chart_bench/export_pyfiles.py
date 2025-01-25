import os  
import json  
from tqdm import tqdm

# 设置目录路径  
# directory_path = '/mnt/lingjiejiang/multimodal_code/data/chart_data/github_chart'  
output_file_path = "/mnt/lingjiejiang/multimodal_code/data/chart_data/ChartBench/charbench_4o_revised_64k.json"
# save_directory_path = 'ourdata_revise/code'  

base_dir = "/mnt/lingjiejiang/multimodal_code/data/chart_data/ChartBench/chart_bench_4o_img"
# 确保保存目录存在  
# os.makedirs(save_directory_path, exist_ok=True)  
  
# 读取 JSON 数据  
with open(output_file_path, 'r') as f:  
    chart_data = json.load(f)  
  
# chart_data = chart_data[:10]
# 更新 ID 并保存前 50 个文本到文件  
for idx, item in tqdm(enumerate(chart_data), desc="Processing Files", total=len(chart_data)):  
    # 更新 ID 为五位数格式  
    # index = item['index']
    # item['id'] = f"{index + 1:06d}"  
    
    # 只处理前 1000000 个项目  
    # if idx < 1000:  
    # 获取文本内容  
    text_content = item['code_text']  
    
    # 保存文件路径  
    # file_path = os.path.join(save_directory_path, f"{item['id']}.py")  
    file_path = item["images"].replace(".jpg", ".py")
    file_path = os.path.join("/mnt/lingjiejiang/multimodal_code/data/chart_data/ChartBench/gpt4o_code",
                                os.path.relpath(item["images"], base_dir)).replace(".jpg", ".py")
    directory = os.path.dirname(file_path)
    os.makedirs(directory, exist_ok=True)
    # 写入文本到文件  
    with open(file_path, 'w') as py_file:  
        py_file.write(text_content)  
  
print("处理完成，前 1000000 个文件已保存。")  