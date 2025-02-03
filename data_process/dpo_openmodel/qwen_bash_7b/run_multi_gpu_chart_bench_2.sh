#!/bin/bash

CUDA_VISIBLE_DEVICES=0,1 python data_process/dpo_openmodel/html_generate_7b.py \
    --model_name Qwen2-VL-7B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/vlm_checkpoints/Qwen2-VL-7B-Instruct \
    --batch_size 64 \
    --start_index 75238 \
    --end_index 94047 \
    --output_dir /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_generate_htmlchart150k_2 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_log/dpo_2_75238_94047.log &
CUDA_VISIBLE_DEVICES=2,3 python data_process/dpo_openmodel/html_generate_7b.py \
    --model_name Qwen2-VL-7B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/vlm_checkpoints/Qwen2-VL-7B-Instruct \
    --batch_size 64 \
    --start_index 94047 \
    --end_index 112856 \
    --output_dir /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_generate_htmlchart150k_2 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_log/dpo_2_94047_112856.log &
CUDA_VISIBLE_DEVICES=4,5 python data_process/dpo_openmodel/html_generate_7b.py \
    --model_name Qwen2-VL-7B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/vlm_checkpoints/Qwen2-VL-7B-Instruct \
    --batch_size 64 \
    --start_index 112856 \
    --end_index 131665 \
    --output_dir /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_generate_htmlchart150k_2 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_log/dpo_2_112856_131665.log &
CUDA_VISIBLE_DEVICES=6,7 python data_process/dpo_openmodel/html_generate_7b.py \
    --model_name Qwen2-VL-7B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/vlm_checkpoints/Qwen2-VL-7B-Instruct \
    --batch_size 64 \
    --start_index 131665 \
    --end_index 150476 \
    --output_dir /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_generate_htmlchart150k_2 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_log/dpo_2_131665_150476.log &

wait
