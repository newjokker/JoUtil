# 说明


* yolov5RT 是放在 lib 中的 dete_libs 中的

* fwd : 服务端

* khd_rtsp 客户端

* allflow.py 和 客户端，服务端，放在一个文件夹，与 lib 同级

* 服务端指定了需要的环境的路径，当换了docker 的时候需要进行调整

* yolov5RT 里面也指定了固定环境地址，后面是否高程相对的地址




### 运行

* 使用的镜像 tensorrt:v0.0.4

* docker run -v /home/ldq/tensorrt_logs:/home/tensorRT/tensorrt_test/logs  -p 1211:1211  -it --gpus 'device=0'  tensorrt:v0.0.4  /bin/bash

[//]: # (* docker run  -p 1211:1211  -it --gpus 'device=0'  tensorrt:v0.0.4  /bin/bash)

* cd /home/tensorRT/tensorrt_test

* python allflow.py 

