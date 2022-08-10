# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# uc 相关的下载操作
import os

import requests
from .ucDatasetOpt import UcDataset, UcDatasetOpt
from .jsonInfo import JsonInfo
from ..utils.FileOperationUtil import FileOperationUtil

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
            img_url = f"http://{self.ip}:{self.port}/image/{each_uc}.jpg"
            json_url = f"http://{self.ip}:{self.port}/json/{each_uc}.json"

            save_json_path = os.path.join(save_json_dir, f"{each_uc}.json")
            save_img_path = os.path.join(save_img_dir, f"{each_uc}.jpg")
            save_xml_path = os.path.join(save_xml_dir, f"{each_uc}.xml")

            if need_img:
                self.load_file_by_url(img_url, save_img_path)

            if need_json or need_xml:
                self.load_file_by_url(json_url, save_json_path)
                if os.path.exists(save_json_path):
                    if need_xml:
                        json_info = JsonInfo(json_path=save_json_path)
                        json_info.save_to_xml(xml_path=save_xml_path)
                else:
                    print(f"* loss json_path or img_path: {each_uc}")

    def save_img_xml_json(self, save_dir, need_numb=None, need_img=True, need_json=False, need_xml=True):

        if need_numb is None:
            uc_list = self.uc_dataset.uc_list
        elif isinstance(need_numb, int) and need_numb > 0:
            uc_list = self.uc_dataset.uc_list[:need_numb]
        else:
            raise ValueError("need_numb need unsingle int")

        self.get_img_json_xml_from_uc_list(uc_list, save_dir=save_dir, need_img=need_img, need_json=need_json, need_xml=need_xml)









