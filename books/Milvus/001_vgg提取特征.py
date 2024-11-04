# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import numpy as np
import torch
import json
import random
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.models as models
from PIL import Image
from JoTools.utils.FileOperationUtil import FileOperationUtil
import requests
from PIL import Image
from io import BytesIO
from JoTools.utils.JsonUtil import JsonUtil
# import pdb

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
        return features.squeeze().cpu().numpy()
    except Exception as e:
        print(e)
        return None

def get_img_by_uc(each_uc, save_path):

    try:
        # 发送 HTTP 请求获取图片内容
        url = f"http://192.168.3.111:11101/file/{each_uc}.jpg"
        response = requests.get(url)
        response.raise_for_status()
        image_content = BytesIO(response.content)
        image = Image.open(image_content)
        image.save(save_path)

    except Exception as e:
        print(f"下载并保存图片时出现错误：{e}")




if __name__ == "__main__":

    # TODO 传入一个 ucd 文件，解析所有的 uc，下载对应的图片，获取 feature 删除图片

    # ---------------------------------------------------------
    img_dir = r"/home/data/ucd_cache/img_cache"
    # img_dir = r"/home/ldq/milvus/all.json"
    save_dir = r"./feature_txt"
    # ---------------------------------------------------------

    device = torch.device("cuda:1" if torch.cuda.is_available() else "cpu")
    vgg = models.vgg19_bn(pretrained=False)
    weights_path = r"./vgg19_bn-c79401a0.pth"
    vgg.load_state_dict(torch.load(weights_path))
    vgg.to(device)
    vgg.eval()

    vgg16_feature_extractor = nn.Sequential(*list(vgg.features.children()))
    avgpool = nn.AdaptiveAvgPool2d((1, 1))

    # pdb.set_trace()

    if os.path.isdir(img_dir):
        img_path_list = list(FileOperationUtil.re_all_file(img_dir, endswitch=[".jpg", ".png", ".JPG", ".PNG"]))
        random.shuffle(img_path_list)

        for index, each_img_path in enumerate(img_path_list):
            each_uc = FileOperationUtil.bang_path(each_img_path)[1]
            each_save_dir = os.path.join(save_dir, each_uc[:3])
            os.makedirs(each_save_dir, exist_ok=True)
            save_txt_path = os.path.join(each_save_dir, each_uc + ".txt")

            if not os.path.exists(save_txt_path):
                print(index, each_img_path)
                features = extract_features(each_img_path)
                if isinstance(features, np.ndarray):
                    np.savetxt(save_txt_path, features)

    elif img_dir[-5:] == ".json":

        uc_list = JsonUtil.load_data_from_json_file(img_dir)["uc_list"]
        random.shuffle(uc_list)

        for index, each_uc in enumerate(uc_list):
            each_img_path = os.path.join(save_dir, f"./{each_uc}.jpg")
            each_save_dir = os.path.join(save_dir, each_uc[:3])
            os.makedirs(each_save_dir, exist_ok=True)
            save_txt_path = os.path.join(each_save_dir, each_uc + ".txt")

            if not os.path.exists(save_txt_path):
                print(index, each_img_path)
                get_img_by_uc(each_uc, each_img_path)
                features = extract_features(each_img_path)
                if isinstance(features, np.ndarray):
                    np.savetxt(save_txt_path, features)

            if os.path.exists(each_img_path):
                os.remove(each_img_path)
