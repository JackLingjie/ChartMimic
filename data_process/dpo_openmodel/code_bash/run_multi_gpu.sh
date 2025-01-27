#!/bin/bash

CUDA_VISIBLE_DEVICES=0 python data_process/dpo_openmodel/code_generate.py \
    --model_name Meta-Llama-3.1-8B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/sft_merge_checkpoints/Meta-Llama-3.1-8B-Instruct \
    --batch_size 256 \
    --start_index 0 \
    --end_index 11906 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Meta-Llama-3.1-8B-Instruct_log/dpo_0_11906.log &
CUDA_VISIBLE_DEVICES=1 python data_process/dpo_openmodel/code_generate.py \
    --model_name Meta-Llama-3.1-8B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/sft_merge_checkpoints/Meta-Llama-3.1-8B-Instruct \
    --batch_size 256 \
    --start_index 11906 \
    --end_index 23812 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Meta-Llama-3.1-8B-Instruct_log/dpo_11906_23812.log &
CUDA_VISIBLE_DEVICES=2 python data_process/dpo_openmodel/code_generate.py \
    --model_name Meta-Llama-3.1-8B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/sft_merge_checkpoints/Meta-Llama-3.1-8B-Instruct \
    --batch_size 256 \
    --start_index 23812 \
    --end_index 35718 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Meta-Llama-3.1-8B-Instruct_log/dpo_23812_35718.log &
CUDA_VISIBLE_DEVICES=3 python data_process/dpo_openmodel/code_generate.py \
    --model_name Meta-Llama-3.1-8B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/sft_merge_checkpoints/Meta-Llama-3.1-8B-Instruct \
    --batch_size 256 \
    --start_index 35718 \
    --end_index 47624 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Meta-Llama-3.1-8B-Instruct_log/dpo_35718_47624.log &
CUDA_VISIBLE_DEVICES=4 python data_process/dpo_openmodel/code_generate.py \
    --model_name Meta-Llama-3.1-8B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/sft_merge_checkpoints/Meta-Llama-3.1-8B-Instruct \
    --batch_size 256 \
    --start_index 47624 \
    --end_index 59530 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Meta-Llama-3.1-8B-Instruct_log/dpo_47624_59530.log &
CUDA_VISIBLE_DEVICES=5 python data_process/dpo_openmodel/code_generate.py \
    --model_name Meta-Llama-3.1-8B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/sft_merge_checkpoints/Meta-Llama-3.1-8B-Instruct \
    --batch_size 256 \
    --start_index 59530 \
    --end_index 71436 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Meta-Llama-3.1-8B-Instruct_log/dpo_59530_71436.log &
CUDA_VISIBLE_DEVICES=6 python data_process/dpo_openmodel/code_generate.py \
    --model_name Meta-Llama-3.1-8B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/sft_merge_checkpoints/Meta-Llama-3.1-8B-Instruct \
    --batch_size 256 \
    --start_index 71436 \
    --end_index 83342 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Meta-Llama-3.1-8B-Instruct_log/dpo_71436_83342.log &
CUDA_VISIBLE_DEVICES=7 python data_process/dpo_openmodel/code_generate.py \
    --model_name Meta-Llama-3.1-8B-Instruct \
    --model_path /mnt/lingjiejiang/textual_aesthetics/model_checkpoint/sft_merge_checkpoints/Meta-Llama-3.1-8B-Instruct \
    --batch_size 256 \
    --start_index 83342 \
    --end_index 95251 | tee -a /mnt/lingjiejiang/multimodal_code/data/dpo/Meta-Llama-3.1-8B-Instruct_log/dpo_83342_95251.log &

wait
