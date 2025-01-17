export PROJECT_PATH=.
model_name=qwen2vl
# export YOUR_RESULT_DIR=results/direct/chart2code_gpt-4o_DirectAgent_results/direct

# evaluation_dir=${YOUR_RESULT_DIR}
evaluation_dir=results/direct/chart2code_${model_name}_DirectAgent_results/direct

python chart2code/main_selfmodel.py --cfg_path eval_configs/evaluation_direct.yaml --tasks gpt4evaluation --evaluation_dir ${evaluation_dir} --model ${model_name}