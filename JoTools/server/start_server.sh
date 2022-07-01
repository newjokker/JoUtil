#!/bin/bash

echo "start serve"

host=${host:-0.0.0.0}
port=${port:-11123}
img_dir=${img_dir}


echo "port : {$port}"
echo "host : {$host}"
echo "img_dir : {$img_dir}"

# 将 allflow 的结果保存在指定的目录下面
python3 /home/txkj/scripts/map_depto.py --host "$host" --port "$port" --img_dir "$img_dir"

echo "stop serve"
