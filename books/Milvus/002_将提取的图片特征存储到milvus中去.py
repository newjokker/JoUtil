# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import random
import time
import numpy as np
from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
)
from JoTools.utils.FileOperationUtil import FileOperationUtil


def get_entities(txt_dir, step=10000):
    entities = [[], []]
    index = 0
    for each_img_path in FileOperationUtil.re_all_file(txt_dir, endswitch=[".txt"]):
        index += 1
        each_uc = FileOperationUtil.bang_path(each_img_path)[1]
        each_feature = np.loadtxt(each_img_path).tolist()
        entities[0].append(each_uc)
        entities[1].append(each_feature)

        if index >= step:
            yield entities
            index = 0
            entities = [[], []]

    if entities[0]:
        yield entities


if __name__ == "__main__":


    # --------------------------------------------------------
    COLLECTION_NAME = "uc_milvus"
    # txt_dir = r"./feature_txt"
    txt_dir = r"C:\Users\14271\Desktop\feature_txt"
    # --------------------------------------------------------


    # connections.connect("default", host="localhost", port="19530")
    connections.connect("default", host="192.168.3.221", port="19530")
    has = utility.has_collection(COLLECTION_NAME)

    print(has)

    if has:
        utility.drop_collection(COLLECTION_NAME)

    fields = [
        FieldSchema(name="pk", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="uc", dtype=DataType.VARCHAR, auto_id=False, max_length=7),
        FieldSchema(name="feature", dtype=DataType.FLOAT_VECTOR, dim=512)
    ]


    schema          = CollectionSchema(fields, f"{COLLECTION_NAME} is the simplest demo to introduce the APIs")
    uc_milvus       = Collection(f"{COLLECTION_NAME}", schema, consistency_level="Strong")

    for each_entities in get_entities(txt_dir):
        start = time.time()
        insert_result   = uc_milvus.insert(each_entities)
        print(f"Number of entities in Milvus: {uc_milvus.num_entities}, use time {time.time() - start}")  # check the num_entites
