# 向量数据库

### 启动服务

* 官方的参考文档: https://milvus.io/docs/install_standalone-docker.md

* 安装 docker-compose
  * git@github.com:docker/compose.git 项目下面找发布的版本
  * 使用过的下载链接: https://github.com/docker/compose/releases/download/v2.23.3/docker-compose-linux-x86_64
  * 将下载后的文件重命名为 docker-compose 放在 /usr/local/bin/ 下面，就可以直接使用 docker-compose 命令了 
  
* 下载配置文件 
  * https://github.com/milvus-io/milvus/releases/download/v2.3.3/milvus-standalone-docker-compose.yml

* 启动服务
  * docker-compose up -d -f docker-compose.yml (应该有 -f 关键字，如果不使用这个关键字那么将配置文件重命名为 docker-compose.yml)


### 使用 SDK 版本

* pip install pymilvus 


