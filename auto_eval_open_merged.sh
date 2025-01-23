#!/bin/bash  
  
# 定义一个数组，包含所有需要处理的模型名称和路径  
model_names=(  
    "stage2_llm_2nodes_1e5_web2code_bsz128_1e5_chart_evol_40k_282"
    "stage2_llm_2nodes_1e5_web2code_bsz128_1e5_code20_html80_mix_100k_705"

    # "stage2_llm_2nodes_1e5_web2code_bsz128_1e5_web2code_rick_revised_750k_v1_500"
    # "stage2_llm_2nodes_1e5_web2code_bsz128_1e5_web2code_rick_revised_750k_v1_1000"
    # "stage2_llm_2nodes_1e5_web2code_bsz128_1e5_web2code_rick_revised_750k_v1_1500"
    # "stage2_llm_2nodes_1e5_web2code_bsz128_1e5_web2code_rick_revised_html_tag_750k_v2_500"
    # "stage2_llm_2nodes_1e5_web2code_bsz128_1e5_web2code_rick_revised_html_tag_750k_v2_1000"
    # "stage2_llm_2nodes_1e5_web2code_bsz128_1e5_web2code_rick_revised_html_tag_750k_v2_1500"
    # "stage2_llm_2nodes_1e5_web2code_bsz128_1e5_chart52k_369"
    # "stage2_llm_2nodes_1e5_web2code_bsz128_1e5_img_revised_80k_v1-563"
    # "stage2_llm_2nodes_1e5_web2code_bsz128_1e5_img_revised_html_tag_80k_v2-563"
    # "stage2_llm_2nodes_1e5_web2code_bsz128_1e5_web2code_rick_760k_prompt_added_v2_2000"
    # "stage2_llm_2nodes_1e5_web2code_bsz128_1e5_web2code_rick_760k_prompt_added_v2_3000"
    # "stage2_llm_2nodes_1e5_web2code_bsz128_1e5_web2code_rick_760k_prompt_added_v2_4000"
    # "stage2_llm_2nodes_1e5_web2code_bsz128_1e5_web2code_rick_760k_v1_2000"
    # "stage2_llm_2nodes_1e5_web2code_bsz128_1e5_web2code_rick_760k_v1_3000"
    # "stage2_llm_2nodes_1e5_web2code_bsz128_1e5_web2code_rick_760k_v1_4000"
)  
  
# 确保日志目录存在  
log_dir="eval_log"  
mkdir -p "$log_dir"  
  
# 初始化一个用于存储日志文件名的变量  
log_file_prefix=""  
  
# 通过循环最多提取两个模型名称来生成日志文件名  
for ((i = 0; i < ${#model_names[@]} && i < 2; i++)); do  
    # 提取模型名称部分  
    IFS=',' read -r model_name <<< "${model_names[i]}"  
      
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
for model_name in "${model_names[@]}"; do  
    # IFS=',' read -r model_name <<< "$model_info"  
    echo "正在处理模型: $model_name" | tee -a "$log_file"  
      
    # 调用 scripts/auto_run_openmodel.sh 并传入 model_name 和 model_path，将输出追加到同一个日志文件  
    bash scripts/auto_eval_qwen_merged.sh "$model_name"  2>&1 | tee -a "$log_file"  
done  
  
echo "所有模型处理完成。" | tee -a "$log_file"  