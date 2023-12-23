# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import requests
import base64
import json
from flask import Flask, request, jsonify
from JoTools.utils.FileOperationUtil import FileOperationUtil
from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
)

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        base64_encoded = base64.b64encode(image_file.read()).decode('utf-8')
        return base64_encoded




if __name__ == "__main__":


    # ----------------------------------------

    img_path = r"C:\Users\14271\Desktop\del\122.jpg"
    url = r"http://192.168.3.221:50011/get_feature"
    COLLECTION_NAME = "uc_milvus"

    # ----------------------------------------

    img_bs64 = image_to_base64(img_path)
    res = requests.post(url=url, json={'img_bs64': img_bs64})
    res = json.loads(res.text)

    if res["status"] == "correct":
        feature = res["feature"]

        connections.connect("default", host="192.168.3.221", port="19530")

        index = {
            "index_type": "IVF_FLAT",
            # "metric_type": "l2",
            "params": {"nlist": 128},
        }

        fields = [
            FieldSchema(name="uc", dtype=DataType.VARCHAR, is_primary=True,auto_id=False, max_length=7),
            FieldSchema(name="feature", dtype=DataType.FLOAT_VECTOR, dim=512)
        ]

        schema          = CollectionSchema(fields, f"{COLLECTION_NAME} is a demo")
        uc_milvus       = Collection(COLLECTION_NAME, schema, consistency_level="Strong")
        uc_milvus.load()

        search_params = {
            # "metric_type": "l2",
            "params": {"nprobe": 10},
        }

        #
        result = uc_milvus.search([feature], "feature", search_params, limit=5, output_fields=["uc"])

        for hits in result[0]:
            hits = hits.to_dict()
            print(hits["entity"]["uc"], " : ", str(hits["distance"]).ljust(20, " ") , f"http://192.168.3.111:11101/file/{hits['id']}.jpg")





