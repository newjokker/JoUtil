# -*- coding: utf-8  -*-
# -*- author: jokker -*-
import os.path

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
    img_path = r"C:\Users\14271\Desktop\img\Dpb000i.jpg"
    url = r"http://192.168.3.221:50011/get_similar_uc"
    COLLECTION_NAME = "uc_milvus"
    # ----------------------------------------

    img_bs64 = image_to_base64(img_path)
    res = requests.post(url=url, json={'img_bs64': img_bs64, "limit": 3})
    res = json.loads(res.text)

    if res["status"] == "correct":
        for hits in res["uc_info"]:
            print(hits["entity"]["uc"], " : ", str(hits["distance"]).ljust(20, " ") , f"http://192.168.3.111:11101/file/{hits['id']}.jpg")





