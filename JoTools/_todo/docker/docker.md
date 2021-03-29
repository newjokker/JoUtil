# docker


### 基本概念

* 是否安装了 docker 
    * which docker
    * sudo docker run hello-world

* 版本信息
    * docker version

*   Hello Word
    * docker run ubuntu:15.10 /bin/echo "Hello world"
    * ubuntu:15.10 指定要运行的镜像，Docker 首先从本地主机上查找镜像是否存在，如果不存在，Docker 就会从镜像仓库 Docker Hub 下载公共镜像。
    * /bin/echo "Hello world": 在启动的容器里执行的命令

* 交互式容器
    * sudo docker run -i -t -d ubuntu:15.10 /bin/bash
        * -t: 在新容器内指定一个伪终端或终端
        * -i: 允许你对容器内的标准输入 (STDIN) 进行交互
        * -d: 后台运行
            * 加了 -d 参数默认不会进入容器，想要进入容器需要使用指令 docker exec
        
* 退出容器
    * exit
    * ctrl + d

* 创建一个以进程方式运行的容器
    * docker run -d ubuntu:15.10 /bin/sh -c "while true; do echo hello world; sleep 1; done"
    * docker ps , 查看运行的容器
        * CONTAINER ID: 容器 ID。
        * IMAGE: 使用的镜像。
        * COMMAND: 启动容器时运行的命令。
        * CREATED: 容器的创建时间。
        * STATUS: 容器状态。
            * created（已创建）
            * restarting（重启中）
            * running 或 Up（运行中）
            * removing（迁移中）
            * paused（暂停）
            * exited（停止）
            * dead（死亡）
        * PORTS: 容器的端口信息和使用的连接类型（tcp\udp）。
        * NAMES: 自动分配的容器名称。

* 查看容器
    * docker ps 
    * docker ps -a, 查看所有容器，包括已关闭的

* 查看输出
    * docker logs 2b1b7a428627

* 停止容器
    * docker stop id

* 启动一个已经停止的容器
    * docker start id 


### 容器操作

* 进入容器
    * 在使用 -d 参数时，容器启动后会进入后台。此时想要进入容器，可以通过以下指令进入
    * docker attach id
    * docker exec -it id /bin/bash : 推荐大家使用 docker exec 命令，因为此退出容器终端，不会导致容器的停止。

* 导出
    * docker export 1e560fca3906 > ubuntu.tar

* 打包
    * docker commit afcaf46e8305 centos-vim
    * 将容器打包为镜像，运行镜像后得到一个容器，修改这个容器，commit 之后得到修改后的容器对应的镜像

* 导入
    * 

* 删除
    * docker rm -f id

### 镜像操作

* 列出本地主机上的镜像
    * docker images
        * REPOSITORY：表示镜像的仓库源
        * TAG：镜像的标签
        * IMAGE ID：镜像ID
        * CREATED：镜像创建时间
        * SIZE：镜像大小
    
* 运行一个镜像
    * docker run -i -t nc_test:v1 /bin/bash
    * nc_test 镜像的名字
    * :v1 镜像的版本号
    * /bin/bash, ？

* 创建镜像

* 删除镜像

* 查找镜像
    * 查找官方仓库中的镜像
    * docker search ubuntu

* 拖取镜像
    * 下载镜像到本地
    * docker pull ubuntu 

* 保存镜像
    * 

### 仓库操作

* 

### 如何与调度代码配合

---

### docker 操作流程

#### tar | images | container 


* tar --> image 
    * images : docker load image_id
    * container : docker import container_id  

* images|container --> tar
    * images : docker save image_id
    * container : docker export container_id 

* container --> tar
    * docker export 1e560fca3906 > ubuntu.tar

* images --> container
    * docker run -itd image_id /bin/bash

* container --> images
    * docker commit afcaf46e8305 centos-vim

* del container | images
    * 删除镜像时需要从先删除从镜像实例化的所有container，删除container要用 rm 而不是 stop 
    * images : docker rmi image_id
    * container : docker rm container_id 
    * container : docker stop container_id
    * del all container : docker rm $(docker ps -aq)
        * -a : all
        * -q : Only display container IDs




* 进入这个容器进行操作
    * docker exec id -it /bin/bash






































