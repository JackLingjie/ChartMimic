#!/bin/bash

# 定义节点配置文件的路径
NODES_FILE="data_process/dpo_openmodel/config/nodes.txt"

script=$(cat << 'EOF'
cd /tmp

# 检查目录是否存在
if [ -d "ChartMimic" ]; then
    cd ChartMimic
    git fetch origin
else
    git clone https://github.com/JackLingjie/ChartMimic.git
    cd ChartMimic
fi

# 检查并切换到dev分支
current_branch=$(git rev-parse --abbrev-ref HEAD)
if [ "$current_branch" != "dev" ]; then
    git checkout -b dev origin/dev || git checkout dev
fi

git clone https://github.com/JackLingjie/ChartMimic.git

git checkout -b dev origin/dev
pip install -r requirements.txt
pip install --user vllm==0.6.4
pip install -U flash-attn==2.7.2.post1 --no-build-isolation
pip install qwen_vl_utils
EOF
)

pdsh -R ssh -w ^$NODES_FILE "bash -c '$script'"