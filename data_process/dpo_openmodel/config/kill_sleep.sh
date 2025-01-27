#!/bin/bash
set -x
# 定义节点配置文件的路径
NODES_FILE="data_process/dpo_openmodel/config/nodes.txt"

script=$(cat << 'EOF'
kill $(pgrep -f run_gpu)
EOF
)

pdsh -R ssh -w ^$NODES_FILE "bash -c '$script'"