export PROJECT_PATH=.
export YOUR_RESULT_DIR=results/direct/chart2code_gpt-4o_DirectAgent_results/direct

evaluation_dir=${YOUR_RESULT_DIR}

python chart2code/main.py --cfg_path eval_configs/evaluation_direct.yaml --tasks gpt4evaluation --evaluation_dir ${evaluation_dir}