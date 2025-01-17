export PROJECT_PATH=.

model_name=gpt-4o-mini
## low level evaluation
# python chart2code/main_selfmodel.py --cfg eval_configs/direct/code4evaluation.yaml --tasks code4evaluation --model "${model_name}"

## high level evaluation
evaluation_dir=results/direct/chart2code_${model_name}_DirectAgent_results/direct

python chart2code/main_selfmodel.py --cfg_path eval_configs/evaluation_direct.yaml --tasks gpt4evaluation --evaluation_dir ${evaluation_dir} --model ${model_name}

## get reuslts
python scripts/direct_mimic/merge_resulst.py