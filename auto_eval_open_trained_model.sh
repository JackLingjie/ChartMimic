#!/bin/bash  
  
# 定义一个数组，包含所有需要处理的模型名称和路径  
model_names=(  
    "qwen2_vl_mm_only-7b_3072_bsz128_1e3_pretrain_llava_stage2_1M_job_7660,/mnt/lingjiejiang/multimodal_code/exp/saves/qwen2_vl_mm_only-7b_3072_bsz128_1e3_pretrain_llava_stage2_1M_job/sft/full/checkpoint-7660"
    "qwen2_vl_coder_mn_only-7b_3072_bsz128_1e3_pretrain_mix_114k_job_3072_805,/mnt/lingjiejiang/multimodal_code/exp/saves/qwen2_vl_coder_mn_only-7b_3072_bsz128_1e3_pretrain_mix_114k_job_3072/sft/full/checkpoint-805/"
    "pretrain_mm_only-7b_3072_bsz128_1e3_mix_data_ocr_code_pretrain_578k_1000,/mnt/lingjiejiang/multimodal_code/exp/saves/pretrain_mm_only-7b_3072_bsz128_1e3_mix_data_ocr_code_pretrain_578k/sft/full/checkpoint-1000/"
    "stage2_llm_2nodes_1e5_web2code_bsz128_1e5_web2code_job_fixed-4000,/mnt/lingjiejiang/multimodal_code/sft_checkpoints/stage2_llm_2nodes_1e5_web2code_bsz128_1e5_web2code_job_fixed-4000"
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
    bash scripts/auto_eval_qwen_trainmodel.sh "$model_name" "$model_path" 2>&1 | tee -a "$log_file"  
done  
  
echo "所有模型处理完成。" | tee -a "$log_file"  