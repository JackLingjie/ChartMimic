#!/bin/bash

export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7

python data_process/dpo_openmodel/html_generate_chart_bench.py \
    --model_name Qwen2-VL-72B-Instruct \
    --model_path /mnt/lingjiejiang/multimodal_code/checkpoints/llms/Qwen2-VL-72B-Instruct \
    --start_index 11744 \
    --end_index 23488 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-72B-Instruct_log/dpo_11744_23488_chartbench46k.log

python run_gpu.py
