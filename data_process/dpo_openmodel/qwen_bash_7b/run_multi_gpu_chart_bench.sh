#!/bin/bash

CUDA_VISIBLE_DEVICES=0 python data_process/dpo_openmodel/html_generate_7b_chart_bench.py \
    --model_name Qwen2-VL-7B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/vlm_checkpoints/Qwen2-VL-7B-Instruct \
    --batch_size 64 \
    --start_index 0 \
    --end_index 11744 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_log/dpo_0_11744_chart_bench.log &
CUDA_VISIBLE_DEVICES=1 python data_process/dpo_openmodel/html_generate_7b_chart_bench.py \
    --model_name Qwen2-VL-7B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/vlm_checkpoints/Qwen2-VL-7B-Instruct \
    --batch_size 64 \
    --start_index 11744 \
    --end_index 23488 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_log/dpo_11744_23488_chart_bench.log &
CUDA_VISIBLE_DEVICES=2 python data_process/dpo_openmodel/html_generate_7b_chart_bench.py \
    --model_name Qwen2-VL-7B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/vlm_checkpoints/Qwen2-VL-7B-Instruct \
    --batch_size 64 \
    --start_index 23488 \
    --end_index 35232 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_log/dpo_23488_35232_chart_bench.log &
CUDA_VISIBLE_DEVICES=3 python data_process/dpo_openmodel/html_generate_7b_chart_bench.py \
    --model_name Qwen2-VL-7B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/vlm_checkpoints/Qwen2-VL-7B-Instruct \
    --batch_size 64 \
    --start_index 35232 \
    --end_index 46977 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_log/dpo_35232_46977_chart_bench.log &

wait
