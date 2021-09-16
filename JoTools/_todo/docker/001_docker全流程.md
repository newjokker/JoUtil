
# Docker 我需要会的操作


### Linux 下 docker 的安装

* ubantu docker 的安装，https://www.runoob.com/docker/ubuntu-docker-install.html

### docker 中三个要素之间的关系

* 镜像（image）+ 容器（container）+ 仓库（repository）

* 镜像 ==> 容器，镜像是文件，容器是进程

### 查看

* 镜像，docker image list

* 容器，docker ps

### 进入

* tar，tar ==> 镜像，
    * docker load -i img_name.tar，
    * docker import /root/tomcat.tar jokker_test:v1，import 可以起名，load 不行
    
* 镜像，实例化容器，docker run -id --name CONTAINER_NAME  IMAGE_ID /bin/bash

* 容器，docker exec -it CONTAINER_ID  /bin/bash

### 暂停|执行

* 容器，docker stop CONTAINER_ID
* 容器，docker start CONTAINER_ID

* Ctrl+P+Q，不停止的情况下退出容器

### 退出

* 容器，exit
 
### 删除

* 镜像 docker rmi IMAGE_ID， https://www.runoob.com/docker/docker-rmi-command.html

* 容器 docker rm CONTAINER_ID，https://www.runoob.com/docker/docker-rm-command.html
    
### 保存

* 容器 ==> 镜像，docker commit CONTAINER_ID txkj:v3.5.2
    * 先在容器中 exit
    * docker ps -a 找到刚被关掉的容器的 ID
    * docker commit 容器ID txkj:v1.2.3
    * 完成

* 镜像 ==> tar，docker save -o tar_name image_id ，https://www.runoob.com/docker/docker-save-command.html
    * 直接保存就行 docker save -o txkj:v1.3.5.2.tar imageID 
    * 完成

### 新学会

* 在一行命令后面加 & 就能让命令在后台执行，打印还是正常打印 

* jobs , 查看后台运行的命令

* kill -s 2 1% , 关闭 jobs 中查看到的 index 为 1 的任务  

* dockerfile 的编写与使用

---

### 常用命令

* docker image list

* docker ps
* docker ps -a

* docker run 

* docker exec

* docker rm 
* docker rmi

* docker commit 

* docker save

* docker load 


### 组合命令

* docker run --gpus '"device=0"'  -p 8000:8084 -m 30g  -it txkj:v4.0.0 /bin/bash 


### 样板间的实践

* 调度代码跑不了 : 
    * 少了 --gpus 参数 ， 查不到 gpu 管理 GPU 的模块就会出现问题
    * docker 版本太低，不支持 --gpu  参数
    * 安装 Nvidia_container_Toolkit，参照文件 Nvidia_Container_Toolkit.md
    
* image 和 container
    * docker tag IMAGE_ID REPOSITORY:TAG（仓库：标签） 
    * docker rename CONTAINER_NAME_OLD  CONTAINER_NAME_NEW
    
* tar -> image
    * docker load -i img_name.tar

* 退出容器并保存
    * 在容器中 exit 即可
    * docker ps -a 列出所有没有删除的容器，包括已经暂停的部分
    * docker commit 容器 image_id , 创建新的 image 
    * docker image list , 找到新创建的镜像的 id
    * docker save -o name.tag image_id (这边最好不要使用 image_id 否者重新 load 的时候会出现名字为 none none 的情况，应该使用如 txkj:v0.3.7 这样的命名方式)

* 保存容器
    * 先在容器中 exit
    * docker ps -a 找到刚被关掉的容器的 ID
    * docker commit 容器ID txkj:v1.2.3
    * 完成
    
* 保存镜像为tar包
    * 直接保存就行 docker save -o txkj:v1.3.5.2.tar imageID 
    * 完成

* 映射路径和端口
    * -v 宿主机输入路径:容器路径
    * -p 8000:8084(外面访问的端口号:docker中的端口号)

* dockerfile 
    * 文件内部内容
    * FROM txkj:v3.5.2 
    * CMD ["/modelManageNewTest/startServe.sh"]

    * build 步奏
        * 创建一个新的工作目录
        * cd 进去
        * docker file 文件拷贝进去，文件名不能修改
        * 运行 docker build -t txkj:v3.5.3 .			（把目录下面的所有文件拷贝进去）

* 在命令后面加上 & 就能让命令在后台执行
    * python3 allflow.py &

* 样板间进入参数
    * docker run --gpus '"device=0"' -v /home/suanfa-3/ldq/del/transform_gate:/del -p 8000:8084 -m 30g -e MODEL_TYPES=M1,M2,M3,M4,M5,M6,M7,M8,M9 -e POST_LOC=http://192.168.3.101:3232/dete_res  -e NMS=0.3 -e SCORE=0.6 -it txkj:v3.5.2

* 方天进入参数
    * docker run --gpus device=0 -v /home/suanfa-3/ldq/del/fangtian_test/input_dir:/usr/input_picture -v /home/suanfa-3/ldq/del/fangtian_test/output_dir:/usr/output_dir -v /home/suanfa-3/ldq/del/fangtian_test/json_dir:/usr/input_picture_attach -e MODEL_TYPES=M1,M2,M3,M4,M5,M6,M7,M8,M9 -e NMS=0.6 -e SCORE=0.3 -m 30g -it txkj:v0.2.2 /bin/bash

* docker 中 post 报错的问题
    * 接受的程序端口要改为 0.0.0.0 这种形式，接受任何机器的推送
    * docker 里面指定推送的目标服务器，必须使用 192.168.3.101 这种形式

    
    
    





