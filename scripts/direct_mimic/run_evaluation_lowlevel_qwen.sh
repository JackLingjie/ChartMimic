export PROJECT_PATH=.

models=(
  "qwen2vl"
)

for model in "${models[@]}"; do
  python chart2code/main_selfmodel.py --cfg eval_configs/direct/code4evaluation.yaml --tasks code4evaluation --model "${model}"
done