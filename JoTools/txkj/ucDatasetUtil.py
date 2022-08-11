# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# uc 相关的下载操作
import os

import requests
from .ucDatasetOpt import UcDataset, UcDatasetOpt
from .jsonInfo import JsonInfo
from ..utils.FileOperationUtil import FileOperationUtil



# todo 使用 CPP 写代码，模仿 git 能方便使用数据，和数据集

# todo 处理找不到图片的情况

"""
uc dataset
-
ucd check 
ucd search key # 是否需要提供，客户自己去查询应该也行
ucd load save_path ucdataset name
ucd update ucdataset path, 名字可能会重复，需要完善
----
uc
-
uc load json_path save_dir 110 ， 第一个是 img 第二个是 xml 第三个是 json ， 1 是下载，0 或者不写就是不下载 
"""


class UCDatasetUtil():

    def __init__(self, json_path:str, ip:str, port:int):
        self.uc_dataset = UcDataset(json_path)
        self.ip = ip
        self.port = port

    @staticmethod
    def load_file_by_url(assign_url, save_path):
        """根据 url 下载图片"""
        try:
            if os.path.exists(save_path):
                print(f"* file exist : {assign_url}")
                return
            else:
                print(f"* load from {assign_url}")
                r = requests.get(assign_url)
                with open(save_path, 'wb') as f:
                    f.write(r.content)
        except Exception as e:
            print(e)
            print(f"load file failed : {assign_url}")

    def get_img_json_xml_from_uc_list(self, uc_list, save_dir, need_img=True, need_json=True, need_xml=True):
        """输入一个 uc_dataset_name 从数据库中获取对应的 img json 和 xml"""
        print('* scan dataset')

        save_json_dir = os.path.join(save_dir, "json")
        save_img_dir = os.path.join(save_dir, "img")
        save_xml_dir = os.path.join(save_dir, "xml")
        os.makedirs(save_json_dir, exist_ok=True)
        os.makedirs(save_img_dir, exist_ok=True)
        os.makedirs(save_xml_dir, exist_ok=True)

        need_file_list = []
        for each_uc in uc_list:
            img_url = f"http://{self.ip}:{self.port}/file/{each_uc}.jpg"
            json_url = f"http://{self.ip}:{self.port}/file/{each_uc}.json"
            xml_url = f"http://{self.ip}:{self.port}/file/{each_uc}.xml"

            save_json_path = os.path.join(save_json_dir, f"{each_uc}.json")
            save_img_path = os.path.join(save_img_dir, f"{each_uc}.jpg")
            save_xml_path = os.path.join(save_xml_dir, f"{each_uc}.xml")

            if need_img:
                self.load_file_by_url(img_url, save_img_path)

            if need_xml:
                self.load_file_by_url(xml_url, save_xml_path)

            if need_json:
                self.load_file_by_url(json_url, save_json_path)

    def save_img_xml_json(self, save_dir, need_numb=None, need_img=True, need_json=False, need_xml=True):

        if need_numb is None:
            uc_list = self.uc_dataset.uc_list
        elif isinstance(need_numb, int) and need_numb > 0:
            uc_list = self.uc_dataset.uc_list[:need_numb]
        else:
            raise ValueError("need_numb need unsingle int")

        self.get_img_json_xml_from_uc_list(uc_list, save_dir=save_dir, need_img=need_img, need_json=need_json, need_xml=need_xml)

    def get_ucdataset_by_uc_list(self):
        """将一系列 uc list 生成对应的 json"""

    def save_ucdataset(self, img_dir):
        """遍历文件夹中的图片，找到符合 uc 规范的，生成一个对应的 ucDataset 用于标记"""
        pass

    def check_ucdataset(self):
        """查看已有的数据集"""
        # todo 分为官方数据集和私人数据集分开显示

    def search_ucdataset(self):
        """根据关键字对uc_dataset 进行查询"""

    def update_ucdataset(self):
        """上传自己的数据集"""

    def delete_ucdataset(self):
        """删除私人数据集"""

    def load_ucdataset(self):
        """下载数据集"""
        # 官方数据集和私人数据集是分开放的
        # 官方数据集是有日期的，私人数据集不强制需要日期
        # 官方数据集只能数据管理员操作，私人数据集可以大家一起操作（1）删除（2）上传（3）下载








