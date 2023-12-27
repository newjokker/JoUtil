# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
import numpy as np
# import torch
# import torch.nn as nn
# import torchvision.transforms as transforms
# import torchvision.models as models
# from PIL import Image
from JoTools.utils.FileOperationUtil import FileOperationUtil
from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
)

COLLECTION_NAME = "uc_milvus"

connections.connect("default", host="192.168.3.33", port="19530")



fields = [
    FieldSchema(name="uc", dtype=DataType.VARCHAR, is_primary=True,auto_id=False, max_length=7),
    FieldSchema(name="feature", dtype=DataType.FLOAT_VECTOR, dim=512)
]

schema          = CollectionSchema(fields, f"{COLLECTION_NAME} is a demo")
uc_milvus       = Collection(COLLECTION_NAME, schema, consistency_level="Strong")


search_params = {
    "metric_type": "L2",
    "params": {"nprobe": 10},
}

expr = 'uc in ["Eei002k", "Eei00q2"]'

uc_milvus.delete(expr)





