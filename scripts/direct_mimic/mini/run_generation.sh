export PROJECT_PATH=.

model=gpt-4o-mini

python chart2code/main.py \
--cfg_path eval_configs/direct_generation.yaml \
--tasks chart2code \
--model ${model}