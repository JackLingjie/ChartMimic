#!/bin/bash

export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7

python data_process/dpo_openmodel/html_generate.py \
    --model_name Qwen2-VL-72B-Instruct \
    --model_path /mnt/lingjiejiang/multimodal_code/checkpoints/llms/Qwen2-VL-72B-Instruct \
    --start_index 137929 \
    --end_index 150476 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-72B-Instruct_log/dpo_137929_150476.log

python run_gpu.py
