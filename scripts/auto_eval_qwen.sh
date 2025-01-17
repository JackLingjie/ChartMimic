#!/bin/bash
export PROJECT_PATH=.

## generate code
model_name="Qwen2-VL-7B-Instruct"
model_path="/mnt/lingjiejiang/textual_aesthetics/model_checkpoint/vlm_checkpoints/Qwen2-VL-7B-Instruct"

# python batch_generate.py --model_name ${model_name} --model_path ${model_path}

# ## run code
# export PROJECT_PATH=.
# models=(
#   "qwen2vl"
# )

# template_type=direct;agent_type=DirectAgent

# python chart2code/utils/post_process/code_checker.py \
#     --input_file results/direct/chart2code_${model_name}_${agent_type}_results.json \
#     --template_type ${template_type}

# python chart2code/utils/post_process/code_interpreter.py \
#     --input_file results/direct/chart2code_${model_name}_${agent_type}_results.json \
#     --template_type ${template_type}

# ## low level evaluation
# python chart2code/main_selfmodel.py --cfg eval_configs/direct/code4evaluation.yaml --tasks code4evaluation --model "${model_name}"

## high level evaluation
evaluation_dir=results/direct/chart2code_${model_name}_DirectAgent_results/direct

python chart2code/main_selfmodel.py --cfg_path eval_configs/evaluation_direct.yaml --tasks gpt4evaluation --evaluation_dir ${evaluation_dir} --model ${model_name}

## get reuslts
# python scripts/direct_mimic/merge_resulst.py