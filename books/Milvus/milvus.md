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

* 在 221 服务器上部署的服务老师崩溃，在 33 上部署的服务就很稳定，不知道原因

### 使用 SDK 版本

* pip install pymilvus 

### 插入，删除数据

```python
connections.connect("default", host="192.168.3.33", port="19530")
has = utility.has_collection(COLLECTION_NAME)

# 当前的版本好像还没有支持主键去重的功能，所以数据会被重复插入
if has and remove_db_info:
    utility.drop_collection(COLLECTION_NAME)
    print(f"drop collection {COLLECTION_NAME}")

fields = [
    FieldSchema(name="uc", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=7),
    FieldSchema(name="feature", dtype=DataType.FLOAT_VECTOR, dim=512)
]

schema          = CollectionSchema(fields, f"{COLLECTION_NAME} is a demo")
uc_milvus       = Collection(f"{COLLECTION_NAME}", schema, consistency_level="Strong")

# 每次插入的数据过多会报错，就少插入一些
for each_entities in get_entities(txt_dir, 10000):
    start = time.time()
    insert_result   = uc_milvus.insert(each_entities)
    print(f"Number of entities in Milvus: {uc_milvus.num_entities}, use time {time.time() - start}")  # check the num_entites

```

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

### 查询数据

```python
index = {
    "index_type": "IVF_FLAT",
    "metric_type": "L2",
    "params": {"nlist": 128},
}

uc_milvus.create_index("feature", index)    # 不能使用不同的参数新建多个索引，
uc_milvus.load()

search_params = {
    "metric_type": "L2",
    "params": {"nprobe": 10},
}

# 矢量查询
result_1 = uc_milvus.search([assign_feature], "feature", search_params, limit=5, output_fields=["uc"])

# 非矢量数据查询
# 这边可能有一个大坑，就是 必须最外面是单引号，里面是双引号
result_2 = uc_milvus.query(expr='uc in ["Dxd0bd2", "Czr02d9","11234", "Czr02d2"]', output_fields=["uc", "feature"])

```

### 删除数据

```python

# 根据主键删除对应的数据

COLLECTION_NAME = "uc_milvus"
connections.connect("default", host="192.168.3.33", port="19530")

fields = [
    FieldSchema(name="uc", dtype=DataType.VARCHAR, is_primary=True,auto_id=False, max_length=7),
    FieldSchema(name="feature", dtype=DataType.FLOAT_VECTOR, dim=512)
]

schema          = CollectionSchema(fields, f"{COLLECTION_NAME} is a demo")
uc_milvus       = Collection(COLLECTION_NAME, schema, consistency_level="Strong")
expr = 'uc in ["Eei002k", "Eei00q2"]'
uc_milvus.delete(expr)
```

## ucd search_similar 功能

* 指定返回个数
* 返回结果可以生成 ucd 格式的 json





