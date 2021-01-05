# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import cv2
from abc import ABC
from .resBase import ResBase
from .deteObj import DeteObj
from JoTools.utils.JsonUtil import JsonUtil
from JoTools.txkjRes.classifyXml import parse_xml, save_to_xml


class ClassifyResBase(ResBase, ABC):
    """检测结果"""

    def __init__(self, xml_path=None, assign_img_path=None, json_path=None):
        # 子类新方法需要放在前面
        self.tag = None
        super().__init__(xml_path, assign_img_path, json_path)

    def _parse_xml_info(self):
        """解析 xml 中存储的分类结果"""

        xml_info = parse_xml(self.xml_path)
        #
        if 'size' in xml_info:
            if 'height' in xml_info['size']:
                self.height = float(xml_info['size']['height'])
            if 'width' in xml_info['size']:
                self.width = float(xml_info['size']['width'])
        #
        if 'filename' in xml_info:
            self.file_name = xml_info['filename']

        if 'folder' in xml_info:
            self.folder = xml_info['folder']

        if 'tag' in xml_info:
            self.tag = xml_info['tag']

    def _parse_json_info(self, json_dict=None):
        """解析 json 信息"""

        if self.json_path is not None:
            json_info = JsonUtil.load_data_from_json_file(self.json_path)
        elif json_dict is not None:
            json_info = json_dict
        else:
            raise ValueError("json_file_path json_dict 不能同时为空")
        #
        if 'size' in json_info:
            if 'height' in json_info['size']:
                self.height = float(json_info['size']['height'])
            if 'width' in json_info['size']:
                self.width = float(json_info['size']['width'])
        #
        if 'filename' in json_info:
            self.file_name = json_info['filename']

        if 'path' in json_info:
            self.img_path = json_info['path']

        if 'folder' in json_info:
            self.folder = json_info['folder']

        if 'tag' in json_info:
            self.folder = json_info['tag']

    def save_to_xml(self, save_path, assign_tag=None):
        """保存为 xml"""

        if assign_tag is None:
            tag = self.tag
        else:
            tag = assign_tag

        xml_info = {'size':{'height': str(self.height), 'width': str(self.width), 'depth': '3'},
                    'filename': self.file_name, 'path': self.img_path, 'folder': self.folder, 'tag':tag}

        # 保存为 xml
        save_to_xml(xml_info, xml_path=save_path)

    def save_to_json(self, save_path=None, assign_tag=None):
        """保存为 json"""

        if assign_tag is None:
            tag = self.tag
        else:
            tag = assign_tag
        #
        json_dict = {'size': {'height': int(self.height), 'width': int(self.width), 'depth': '3'},
                    'filename': self.file_name, 'path': self.img_path, 'tag':tag, 'folder': self.folder}
        if save_path is None:
            return json_dict
        else:
            JsonUtil.save_data_to_json_file(json_dict, save_path)

    def set_tag(self, assign_tag):
        """设定标签"""
        self.tag = assign_tag


