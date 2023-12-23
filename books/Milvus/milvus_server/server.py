# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import numpy as np
import torch
import json
import random
import uuid
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image
from JoTools.utils.FileOperationUtil import FileOperationUtil
import requests
from io import BytesIO
from JoTools.utils.JsonUtil import JsonUtil
# import pdb
# from gevent import monkey
# from gevent.pywsgi import WSGIServer
from flask import Flask, request, jsonify
import base64
import io
import argparse
from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
)

# monkey.patch_all()

app = Flask(__name__)


def preprocess_image(image_path):
    image = Image.open(image_path).convert("RGB")
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    return transform(image).unsqueeze(0)

def extract_features(image_path):
    try:
        input_image = preprocess_image(image_path).to(device)
        with torch.no_grad():
            features = vgg16_feature_extractor(input_image)
            features = avgpool(features).flatten()
        return features.squeeze().cpu().numpy().tolist()
    except Exception as e:
        print(e)
        return None

def get_img_by_url(url, save_path):

    try:
        response = requests.get(url)
        response.raise_for_status()
        image_content = BytesIO(response.content)
        image = Image.open(image_content)
        image.save(save_path)

    except Exception as e:
        print(f"下载并保存图片时出现错误：{e}")

def get_img_by_bs64(bs64_string, save_path):
    binary_data = base64.b64decode(bs64_string)
    image = Image.open(io.BytesIO(binary_data))
    image.save(save_path)

def get_feature_by_uc_or_bs64(img_url="", img_bs64=""):
    try:
        img_path = f"./{str(uuid.uuid1())}.jpg"

        if img_url:
            get_img_by_url(img_url, img_path)
        elif img_bs64:
            get_img_by_bs64(img_bs64, img_path)

        if os.path.exists(img_path):
            feature = extract_features(img_path)
            os.remove(img_path)
            if feature:
                return feature
            else:
                return "error, extra feature failed"
        else:
            return "error, save img error"

    except Exception as e:
        return f"error, {e}"

@app.route('/get_feature', methods=['post'])
def get_feature():
    """获取检测状态"""

    # TODO 支持对指定 uc 的特征的获取，直接去数据库中查询对应的 uc 的 feature 即可

    try:
        img_url, img_bs64 = "", ""
        json_info = request.get_json()

        if "img_url" in json_info:
            img_url = json_info["img_url"]
        elif "img_bs64" in json_info:
            img_bs64 = json_info["img_bs64"]
        else:
            return jsonify({"status":"error, need img_url or img_bs64"})

        feature = get_feature_by_uc_or_bs64(img_url, img_bs64)

        if isinstance(feature, list):
            return jsonify({"status": "correct", "feature":feature})
        else:
            return jsonify({"status": f"{feature}"})
    except Exception as e:
        return jsonify({"status": f"{e}"})

@app.route('/get_similar_uc', methods=['post'])
def get_similar_uc():

    try:
        img_url, img_bs64 = "", ""
        json_info = request.get_json()

        limit = 5
        if "limit" in json_info:
            limit = json_info["limit"]

        if "img_url" in json_info:
            img_url = json_info["img_url"]
        elif "img_bs64" in json_info:
            img_bs64 = json_info["img_bs64"]
        else:
            return jsonify({"status":"error, need img_url or img_bs64"})

        feature = get_feature_by_uc_or_bs64(img_url, img_bs64)

        if isinstance(feature, list):

            # TODO 查询得到最近似的几个 uc
            search_params = {"params": {"nprobe": 10},}
            result = uc_milvus.search([feature], "feature", search_params, limit=limit, output_fields=["uc"])
            res = []
            for hits in result[0]:
                res.append(hits.to_dict())

            return jsonify({"status": "correct", "uc_info": res})
        else:
            return jsonify({"status": f"{feature}"})
    except Exception as e:
        return jsonify({"status": f"{e}"})

@app.route('/insert_uc_list')
def insert_uc_list():
    """当前插入的只能是已经入库的数据，插入之间需要进行检查，检查数据库里面是否包含当前的 uc"""

    def if_uc_in_db():
        """数据库中是否有对应的 uc"""
        pass

    # TODO 插入数据

    # TODO 更新查询字典

# def server_start():
#     global host, port
#     http_server = WSGIServer((host, port), app)
#     http_server.serve_forever()

def parse_args():
    parser = argparse.ArgumentParser(description='Tensorflow Faster R-CNN demo')
    parser.add_argument('--port', dest='port', type=int, default=50011)
    parser.add_argument('--host', dest='host', type=str, default='0.0.0.0')
    parser.add_argument('--tmp_dir', dest='tmp_dir', type=str, default="./")
    # parser.add_argument('--gpu_id', dest='gpu_id', type=int, default=0)
    parser.add_argument('--weight_path', dest='weight_path', type=str, default=r"./data/vgg19_bn-c79401a0.pth")
    #
    args = parser.parse_args()
    return args


if __name__ == "__main__":


    args            = parse_args()
    port            = args.port
    host            = args.host
    tmp_dir         = args.tmp_dir
    weights_path    = args.weight_path

    print(f"host : {host}")
    print(f"port : {port}")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # get vgg model
    vgg = models.vgg19_bn(pretrained=False)
    vgg.load_state_dict(torch.load(weights_path))
    vgg.to(device)
    vgg.eval()
    print("* load vgg success")

    vgg16_feature_extractor = nn.Sequential(*list(vgg.features.children()))
    avgpool = nn.AdaptiveAvgPool2d((1, 1))

    # connect milvus
    COLLECTION_NAME = "uc_milvus"
    connections.connect("default", host="192.168.3.221", port="19530")
    fields = [  FieldSchema(name="uc", dtype=DataType.VARCHAR, is_primary=True,auto_id=False, max_length=7),
                FieldSchema(name="feature", dtype=DataType.FLOAT_VECTOR, dim=512)]
    schema          = CollectionSchema(fields, f"{COLLECTION_NAME} is a demo")
    uc_milvus       = Collection(COLLECTION_NAME, schema, consistency_level="Strong")
    uc_milvus.load()
    print("* load milvus success")

    #
    app.run(debug=True, host=host, port=port)



