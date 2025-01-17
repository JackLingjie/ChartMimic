#!/bin/bash  
  
# 定义一个数组，包含所有需要处理的模型名称和路径  
model_names=(  
    "Llama-3.2-11B-Vision-Instruct,/mnt/lingjiejiang/textual_aesthetics/model_checkpoint/vlm_checkpoints/Llama-3.2-11B-Vision-Instruct"  
    "llava-onevision-qwen2-7b-ov-hf,/mnt/lingjiejiang/textual_aesthetics/model_checkpoint/vlm_checkpoints/llava-onevision-qwen2-7b-ov-hf"  
    "MiniCPM-V-2_6,/mnt/lingjiejiang/textual_aesthetics/model_checkpoint/vlm_checkpoints/MiniCPM-V-2_6"  

)  
  
# 确保日志目录存在  
log_dir="eval_log"  
mkdir -p "$log_dir"  
  
# 初始化一个用于存储日志文件名的变量  
log_file_prefix=""  
  
# 通过循环最多提取两个模型名称来生成日志文件名  
for ((i = 0; i < ${#model_names[@]} && i < 2; i++)); do  
    # 提取模型名称部分  
    IFS=',' read -r model_name _ <<< "${model_names[i]}"  
      
    # 替换非法文件名字符（如果有）  
    sanitized_name="${model_name//\//_}"  
      
    if [ -z "$log_file_prefix" ]; then  
        log_file_prefix="$sanitized_name"  
    else  
        log_file_prefix="${log_file_prefix}_${sanitized_name}"  
    fi  
done 
  
# 生成完整的日志文件路径  
log_file="${log_dir}/${log_file_prefix}.log"  
  
# 清空日志文件  
> "$log_file"  

echo "开始处理所有模型..." | tee -a "$log_file"  
  
# 循环遍历数组中的每个模型名称  
for model_info in "${model_names[@]}"; do  
    IFS=',' read -r model_name model_path <<< "$model_info"  
    echo "正在处理模型: $model_name" | tee -a "$log_file"  
      
    # 调用 scripts/auto_run_openmodel.sh 并传入 model_name 和 model_path，将输出追加到同一个日志文件  
    bash scripts/auto_run_openmodel.sh "$model_name" "$model_path" 2>&1 | tee -a "$log_file"  
done  
  
echo "所有模型处理完成。" | tee -a "$log_file"  