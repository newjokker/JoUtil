# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import copy
import os
import pickle
import redis
from PIL import Image
from abc import ABCMeta, abstractmethod
# from ..utils.DecoratorUtil import DecoratorUtil


class ResBase():

    def __init__(self, xml_path=None, assign_img_path=None, json_dict=None, redis_conn_info=None, img_redis_key=None):
        self.img = None
        self.height = -1                # 检测图像的高
        self.width = -1                 # 检测图像的宽
        self.folder = ""                # 图像存在的文件夹
        self.file_name = ""             # 检测图像文件名
        self.img_path = assign_img_path # 对应的原图的路径
        self.xml_path = xml_path        # 可以从 xml 中读取检测结果
        self.json_dict = copy.deepcopy(json_dict)      # json 文件地址，这边防止 json_dit 被改变，直接用深拷贝
        self.redis_conn = None
        self.redis_conn_info = redis_conn_info
        self.img_redis_key = img_redis_key
        # todo 增加一个图片对象，将一张图片的信息存放到内存中

    @abstractmethod
    def save_to_xml(self, save_path, assign_alarms=None):
        """保存为 xml"""
        pass

    @abstractmethod
    def save_to_json(self, assign_alarms=None):
        """保存为 json"""
        pass

    @abstractmethod
    def _parse_xml_info(self):
        """解析 xml 信息"""
        pass

    @abstractmethod
    def _parse_json_info(self):
        """解析 json 信息"""
        pass

    # @DecoratorUtil.time_this
    @abstractmethod
    def _parse_img_info(self):
        """获取图像信息"""

        if self.img is None:
            if self.img_path is not None:
                if os.path.exists(self.img_path):
                    self.img = Image.open(self.img_path)
                else:
                    return False
            else:
                return False

        self.width, self.height = self.img.size
        if self.img_path:
            self.folder = os.path.split(self.img_path)[0]
            self.file_name = os.path.split(self.img_path)[1]
        return True

    def _connect_redis(self):
        """连接 redis"""
        if self.redis_conn_info is not None:
            host, port = self.redis_conn_info
            self.redis_conn = redis.StrictRedis(host=host, port=port, db=0)

    def _parse_img_info_from_redis(self):
        """从 redis 获取图像信息"""
        if (self.redis_conn is not None) and (self.img_redis_key is not None):
            img_byte = self.redis_conn.get(self.img_redis_key)
            if img_byte:
                self.img = pickle.loads(img_byte)
                self._parse_img_info()

    def set_img_to_redis(self, assign_img_key=None):
        """将图片存入 redis"""
        if (self.img is not None) and (self.redis_conn is not None):
            if assign_img_key is not None:
                self.img_redis_key = assign_img_key
            self.redis_conn.set(assign_img_key, pickle.dumps(self.img))


