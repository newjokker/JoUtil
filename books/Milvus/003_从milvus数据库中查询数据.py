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
"""
输入一张图片，返回最相似的图片的 uc
"""

def preprocess_image(image_path):
    image = Image.open(image_path).convert("RGB")
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    return transform(image).unsqueeze(0)

def extract_features(image_path):
    input_image = preprocess_image(image_path)
    with torch.no_grad():
        features = vgg16_feature_extractor(input_image)
        features = avgpool(features).flatten()
    return features.squeeze().numpy()





if __name__ == "__main__":


    COLLECTION_NAME = "uc_milvus"
    txt_path = r"./feature_txt/Dkd/Dkd0bfh.txt"

    # vgg = models.vgg19_bn(pretrained=False)
    # weights_path = r"./vgg19_bn-c79401a0.pth"
    # vgg.load_state_dict(torch.load(weights_path))
    # vgg.eval()
    #
    # vgg16_feature_extractor = nn.Sequential(*list(vgg.features.children()))
    # avgpool = nn.AdaptiveAvgPool2d((1, 1))
    # each_uc = FileOperationUtil.bang_path(each_img_path)[1]
    # assign_feature = extract_features(img_path).tolist()

    assign_feature = np.loadtxt(txt_path).tolist()
    connections.connect("default", host="localhost", port="19530")

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

    schema          = CollectionSchema(fields, f"{COLLECTION_NAME} is the simplest demo to introduce the APIs")
    uc_milvus       = Collection(COLLECTION_NAME, schema, consistency_level="Strong")
    uc_milvus.create_index("feature", index)
    uc_milvus.load()

    search_params = {
        "metric_type": "l2",
        "params": {"nprobe": 10},
    }

    #
    # result = uc_milvus.search(assign_feature, "feature", search_params, limit=3, output_fields=["uc"])
    result = uc_milvus.search([assign_feature], "feature", search_params, limit=3, output_fields=["uc"])

    for hits in result:
        print(hits)


