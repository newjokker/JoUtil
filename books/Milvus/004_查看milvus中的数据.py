# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import time
from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
)

# 查询速度特别慢，最好能有几十个一起查询，这样应该能快好多



COLLECTION_NAME = "uc_milvus"
# connections.connect("default", host="localhost", port="19530")
connections.connect("default", host="192.168.3.221", port="19530")

index = {
    "index_type": "IVF_FLAT",
    "metric_type": "L2",
    "params": {"nlist": 128},
}

fields = [
    FieldSchema(name="pk", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="uc", dtype=DataType.VARCHAR, auto_id=False, max_length=7),
    FieldSchema(name="feature", dtype=DataType.FLOAT_VECTOR, dim=512)
]

schema = CollectionSchema(fields, f"{COLLECTION_NAME} is the simplest demo to introduce the APIs")
uc_milvus = Collection(COLLECTION_NAME, schema, consistency_level="Strong")
uc_milvus.create_index("feature", index)
uc_milvus.load()

search_params = {
    "metric_type": "l2",
    "params": {"nprobe": 10},
}

start_time = time.time()
# result = uc_milvus.search('Dqc046k', "uc", search_params, limit=3, output_fields=["feature"])

# FIXME 必须小括号里面套着大括号，不能大括号里面套着小括号
# result = uc_milvus.query(expr='uc == "Dqc0462k"', output_fields=["feature"])
result = uc_milvus.query(expr='uc in ["Dxd0bd2", "Czr02d9","11234", "Czr02d2"]', output_fields=["uc", "feature"])


end_time = time.time()

print(f"use time : {end_time - start_time}")


for each in result:
    print(each["uc"], " : ", each["feature"][:10])
    # print("-"*100)
