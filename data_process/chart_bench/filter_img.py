import json  
from PIL import Image  
from tqdm import tqdm  
  
# 设置合理的最大像素数和最大宽高  
MAX_PIXELS = 4259840  # 例如：2560 * 1440  
MAX_WIDTH = 2500  
MAX_HEIGHT = 2000 

  
# 读取JSON文件  
save_path = "/mnt/lingjiejiang/multimodal_code/data/chart_data/ChartBench/cot_existing_images_61k.json"  
with open(save_path, 'r') as f:  
    data = json.load(f)  
  
# 遍历每个数据项  
filtered_data = []  
for item in tqdm(data):  
    keep_item = True  
    image_path = item.get('images')  
    if image_path:  
        try:  
            with Image.open(image_path) as img:  
                # 检查图片尺寸  
                if img.width > MAX_WIDTH or img.height > MAX_HEIGHT or (img.width * img.height) > MAX_PIXELS:  
                    keep_item = False  
                    # print(f"Image {image_path} exceeds size limits and will be removed.")  
        except Exception as e:  
            print(f"Could not process image {image_path}: {e}")  
            keep_item = False  
    if keep_item:  
        filtered_data.append(item)  
  
# 输出过滤后的数据长度  
print(f"Number of items after filtering: {len(filtered_data)}")  
  
# 将过滤后的数据保存回JSON文件  
filtered_save_path = f"/mnt/lingjiejiang/multimodal_code/data/chart_data/ChartBench/cot_data_{len(filtered_data) // 1000}k_big_img_filtered.json"  
with open(filtered_save_path, "w") as f:  
    json.dump(filtered_data, f, indent=0)  
print(f"Filtered data saved to {filtered_save_path}")