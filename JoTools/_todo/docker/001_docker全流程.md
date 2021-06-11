
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

### 暂停

* 容器，docker stop CONTAINER_ID

### 退出

* 容器，exit
 
### 删除

* 镜像 docker rmi IMAGE_ID， https://www.runoob.com/docker/docker-rmi-command.html

* 容器 docker rm CONTAINER_ID，https://www.runoob.com/docker/docker-rm-command.html
    
### 保存

* 容器 ==> 镜像，docker commit 

* 镜像 ==> tar，docker save -o tar_name image_id ，https://www.runoob.com/docker/docker-save-command.html

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








