# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import time
from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
)


COLLECTION_NAME = "uc_milvus"
connections.connect("default", host="192.168.3.33", port="19530")


fields = [
    FieldSchema(name="uc", dtype=DataType.VARCHAR, is_primary=True, auto_id=False, max_length=7),
    FieldSchema(name="feature", dtype=DataType.FLOAT_VECTOR, dim=512)
]

schema = CollectionSchema(fields, f"{COLLECTION_NAME} is a demo")
uc_milvus = Collection(COLLECTION_NAME, schema, consistency_level="Strong")

# 从内存中释放 collection
uc_milvus.release()             # 删除索引需要先从内存中释放 collection
uc_milvus.drop_index()          # 删除索引，

# 只有建立索引的时候 metric_type 是 L2, 搜索的时候才能用 L2 距离
index = {
    "index_type": "IVF_FLAT",
    "metric_type": "L2",
    "params": {"nlist": 128},
}

uc_milvus.create_index("feature", index)  # 不能使用不同的参数新建多个索引，
uc_milvus.load()
