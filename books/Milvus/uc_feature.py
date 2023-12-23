# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import random
import time

from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
)


def decimal_to_base36(decimal_number):

    if not isinstance(decimal_number, int):raise ValueError("Input must be an integer")

    if decimal_number == 0:return '0'

    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    base36_representation = ''

    while decimal_number:
        decimal_number, remainder = divmod(decimal_number, 36)
        base36_representation = digits[remainder] + base36_representation

    return base36_representation


connections.connect("default", host="localhost", port="19530")
has = utility.has_collection("uc_milvus")

if has:
    utility.drop_collection("uc_milvus")

fields = [
    FieldSchema(name="pk", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="uc", dtype=DataType.VARCHAR, auto_id=False, max_length=7),
    FieldSchema(name="feature", dtype=DataType.FLOAT_VECTOR, dim=8)
]

schema = CollectionSchema(fields, "uc_milvus is the simplest demo to introduce the APIs")
uc_milvus = Collection("uc_milvus", schema, consistency_level="Strong")
num_entities = 1000

# pk 设置为紫东阁填充的主键，所以不需要显示插入
entities = [
    # provide the pk field because `auto_id` is set to False
    [decimal_to_base36(i) for i in range(num_entities)],
    [[random.random() for _ in range(8)] for _ in range(num_entities)],  # field embeddings
]

insert_result = uc_milvus.insert(entities)

print(f"Number of entities in Milvus: {uc_milvus.num_entities}")  # check the num_entites


index = {
    "index_type": "IVF_FLAT",
    "metric_type": "L2",
    "params": {"nlist": 128},
}

uc_milvus.create_index("feature", index)

uc_milvus.load()

vectors_to_search = entities[-1][-2:]
search_params = {
    "metric_type": "l2",
    "params": {"nprobe": 10},
}

result = uc_milvus.search(vectors_to_search, "feature", search_params, limit=3, output_fields=["uc"])

for hits in result:
    for hit in hits:
        print(f"hit: {hit}, feature field: {hit.entity.get('uc')}")

# 删除数据库
utility.drop_collection("uc_milvus")









