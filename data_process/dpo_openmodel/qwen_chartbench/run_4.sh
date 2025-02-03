#!/bin/bash

export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7

python data_process/dpo_openmodel/html_generate_chart_bench.py \
    --model_name Qwen2-VL-72B-Instruct \
    --model_path /mnt/lingjiejiang/multimodal_code/checkpoints/llms/Qwen2-VL-72B-Instruct \
    --start_index 35232 \
    --end_index 46977 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-72B-Instruct_log/dpo_35232_46977_chartbench46k.log

python run_gpu.py
