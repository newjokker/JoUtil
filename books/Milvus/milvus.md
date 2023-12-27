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

### 新建，删除索引

```python
uc_milvus.release()             # 删除索引需要先从内存中释放 collection
uc_milvus.drop_index()          # 删除索引，

# 只有建立索引的时候 metric_type 是 L2, 搜索的时候才能用 L2 距离
index = {
    "index_type"    : "IVF_FLAT",
    "metric_type"   : "L2",
    "params"        : {"nlist": 128},
}

uc_milvus.create_index("feature", index)    # 不能使用不同的参数新建多个索引，
uc_milvus.load()                            # 将 collection 加载到内存里面
```

## ucd search_similar 功能

* 指定返回个数
* 返回结果生成 ucd 格式的 json
* 




