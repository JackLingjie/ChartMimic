#!/bin/bash

CUDA_VISIBLE_DEVICES=0,1 python data_process/dpo_openmodel/html_generate_7b.py \
    --model_name Qwen2-VL-7B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/vlm_checkpoints/Qwen2-VL-7B-Instruct \
    --batch_size 64 \
    --start_index 0 \
    --end_index 18809 \
    --output_dir /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_generate_htmlchart150k_1 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_log/dpo_1_0_18809.log &
CUDA_VISIBLE_DEVICES=2,3 python data_process/dpo_openmodel/html_generate_7b.py \
    --model_name Qwen2-VL-7B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/vlm_checkpoints/Qwen2-VL-7B-Instruct \
    --batch_size 64 \
    --start_index 18809 \
    --end_index 37618 \
    --output_dir /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_generate_htmlchart150k_1 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_log/dpo_1_18809_37618.log &
CUDA_VISIBLE_DEVICES=4,5 python data_process/dpo_openmodel/html_generate_7b.py \
    --model_name Qwen2-VL-7B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/vlm_checkpoints/Qwen2-VL-7B-Instruct \
    --batch_size 64 \
    --start_index 37618 \
    --end_index 56427 \
    --output_dir /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_generate_htmlchart150k_1 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_log/dpo_1_37618_56427.log &
CUDA_VISIBLE_DEVICES=6,7 python data_process/dpo_openmodel/html_generate_7b.py \
    --model_name Qwen2-VL-7B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/vlm_checkpoints/Qwen2-VL-7B-Instruct \
    --batch_size 64 \
    --start_index 56427 \
    --end_index 75238 \
    --output_dir /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_generate_htmlchart150k_1 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_log/dpo_1_56427_75238.log &

wait
