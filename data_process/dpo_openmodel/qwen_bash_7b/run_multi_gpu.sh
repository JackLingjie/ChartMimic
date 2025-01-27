#!/bin/bash

CUDA_VISIBLE_DEVICES=0 python data_process/dpo_openmodel/html_generate_7b.py \
    --model_name Qwen2-VL-7B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/vlm_checkpoints/Qwen2-VL-7B-Instruct \
    --batch_size 64 \
    --start_index 0 \
    --end_index 37619 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_log/dpo_0_37619.log &
CUDA_VISIBLE_DEVICES=1 python data_process/dpo_openmodel/html_generate_7b.py \
    --model_name Qwen2-VL-7B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/vlm_checkpoints/Qwen2-VL-7B-Instruct \
    --batch_size 64 \
    --start_index 37619 \
    --end_index 75238 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_log/dpo_37619_75238.log &
CUDA_VISIBLE_DEVICES=2 python data_process/dpo_openmodel/html_generate_7b.py \
    --model_name Qwen2-VL-7B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/vlm_checkpoints/Qwen2-VL-7B-Instruct \
    --batch_size 64 \
    --start_index 75238 \
    --end_index 112857 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_log/dpo_75238_112857.log &
CUDA_VISIBLE_DEVICES=3 python data_process/dpo_openmodel/html_generate_7b.py \
    --model_name Qwen2-VL-7B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/vlm_checkpoints/Qwen2-VL-7B-Instruct \
    --batch_size 64 \
    --start_index 112857 \
    --end_index 150476 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Qwen2-VL-7B-Instruct_log/dpo_112857_150476.log &

wait
