# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import copy
import random
import collections
from PIL import Image
import numpy as np
from JoTools.utils.JsonUtil import JsonUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkj.parseXml import parse_xml, save_to_xml
import cv2



class DeteObj(object):
    """检测结果的一个检测对象，就是一个矩形框对应的信息"""

    def __init__(self, x1=None, y1=None, x2=None, y2=None, tag=None, conf=-1):
        self.conf = conf
        self.tag = tag
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def do_offset(self, offset_x, offset_y):
        """对结果进行偏移"""
        self.x1 += offset_x
        self.x2 += offset_x
        self.y1 += offset_y
        self.y2 += offset_y

    def get_rectangle(self):
        """获取矩形范围"""
        return [self.x1, self.y1, self.x2, self.y2]

    def get_center_point(self):
        """得到中心点坐标"""
        # fixme 未测试
        return float(self.x1+self.x2)/2, float(self.y1+self.y2)/2

    def get_format_list(self):
        """得到标准化的 list 主要用于打印"""
        return [str(self.tag), int(self.x1), int(self.y1), int(self.x2), int(self.y2), format(float(self.conf), '.4f')]

    def get_area(self):
        """返回面积，面积大小按照像素个数进行统计"""
        return int(self.x2 - self.x1) * int(self.y2 - self.y1)

    def format_check(self):
        """类型检查和调整"""
        self.conf = float(self.conf)
        self.tag = str(self.tag)
        self.x1 = int(self.x1)
        self.y1 = int(self.y1)
        self.x2 = int(self.x2)
        self.y2 = int(self.y2)
