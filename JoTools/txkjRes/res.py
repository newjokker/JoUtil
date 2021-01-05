# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from PIL import Image
from abc import ABCMeta, abstractmethod


class Res():

    def __init__(self, xml_path=None, assign_img_path=None, json_path=None):
        self.height = -1                # 检测图像的高
        self.width = -1                 # 检测图像的宽
        self.folder = ""                # 图像存在的文件夹
        self.file_name = ""             # 检测图像文件名
        self.img_path = assign_img_path # 对应的原图的路径
        self.xml_path = xml_path        # 可以从 xml 中读取检测结果
        self.json_path = json_path      # json 文件地址

        # 从 xml 中获取检测结果
        if self.xml_path is not None:
            self._parse_xml_info()
        #
        elif self.json_path is not None:
            self._parse_json_info()
        # 解析 img 信息
        if self.img_path is not None:
            self._parse_img_info()

    @abstractmethod
    def save_to_xml(self, save_path, assign_alarms=None):
        """保存为 xml"""
        pass

    @abstractmethod
    def save_to_json(self, save_path=None, assign_alarms=None):
        """保存为 json"""
        pass

    @abstractmethod
    def _parse_xml_info(self):
        """解析 xml 信息"""
        pass

    @abstractmethod
    def _parse_json_info(self, json_dict=None):
        """解析 json 信息"""
        pass

    @abstractmethod
    def _parse_img_info(self):
        """获取图像信息"""
        if self.img_path is not None:
            img = Image.open(self.img_path)
            self.width, self.height = img.size
            self.folder = os.path.split(self.img_path)[0]
            self.file_name = os.path.split(self.img_path)[1]

