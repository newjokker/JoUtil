
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

* 调度代码跑不了 : 少了 --gpus 参数 ， 查不到 gpu 管理 GPU 的模块就会出现问题

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



