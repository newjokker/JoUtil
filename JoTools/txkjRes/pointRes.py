# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import cv2
import copy
import time
import random
from flask import jsonify
import numpy as np
from abc import ABC
from PIL import Image
from .resBase import ResBase
from .deteObj import DeteObj, PointObj
from .deteAngleObj import DeteAngleObj
from ..txkjRes.resTools import ResTools
from ..utils.JsonUtil import JsonUtil
from ..txkjRes.deteXml import parse_xml, save_to_xml, save_to_xml_wh_format
from ..utils.FileOperationUtil import FileOperationUtil
from ..utils.DecoratorUtil import DecoratorUtil
from labelme import utils



class PointRes(ResBase):

    def __init__(self, json_path=None, assign_img_path=None, json_dict=None):
        self._alarms = []
        self.flags = {}
        super().__init__(assign_img_path, json_dict, json_path=json_path)

    def __add__(self, other):
        if not isinstance(other, DeteRes):
            raise TypeError("should be DeteRes")

        res = self.deep_copy()
        for each_point_obj in other:
            if each_point_obj not in self:
                res.add_obj_2(each_point_obj)
        return res

    def __sub__(self, other):
        for each_dete_obj in other:
            self.del_dete_obj(each_dete_obj)
        return self

    def __contains__(self, item):
        if not(isinstance(item, DeteAngleObj) or isinstance(item, DeteObj)):
             raise TypeError("item should 被 DeteAngleObj or DeteObj")

        for each_point_obj in self._alarms:
            if item == each_point_obj:
                return True
        return False

    def __len__(self):
        return len(self._alarms)

    def __getitem__(self, item):
        return self._alarms[index]

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)
        #
        if key == 'img_path' and isinstance(value, str) and self.parse_auto:
            self._parse_img_info()
        elif key == 'json_path' and isinstance(value, str) and self.parse_auto:
            self._parse_json_file()
            pass
        elif key == 'json_dict' and isinstance(value, dict) and self.parse_auto:
            self._parse_json_str()

    @property
    def alarms(self):
        return self._alarms

    def _parse_json_file(self):

        if self.json_path:
            a = JsonUtil.load_data_from_json_file(self.json_path, encoding='GBK')
        else:
            raise ValueError("* self.json_path is none")

        # parse attr
        self.version = a["version"] if "version" in a else ""
        self.image_width = a["imageWidth"] if "imageWidth" in a else ""
        self.image_height = a["imageHeight"] if "imageWidth" in a else ""
        self.img_name = a["imagePath"] if "imagePath" in a else ""
        self.image_data_bs64 = a["imageData"]

        point_index = 0
        for each_shape in a["shapes"]:
            each_shape_type = each_shape["shape_type"]           # 数据的类型 point,
            # todo 点线面分来进行解析
            if each_shape_type == 'point':
                # 解析点
                point_index += 1
                each_label = each_shape["label"]
                each_points_x, each_points_y = each_shape["points"][0]
                new_point = PointObj(each_points_x, each_points_y, each_label, assign_id=point_index)
                self.alarms.append(new_point)

                print(new_point.get_name_str())

    def save_to_json_file(self, save_json_path, include_img_data=False):

        # todo 要想 labelme 能读出来，需要加上 imageData 信息，但是也支持不带 imageData 的 json 生成，可以后期使用函数进行修复，变为可读取即可

        json_info = {"version":"", "imageWidth":"", "imageHeight":"", "imagePath":"", "imageData":"", "shapes":[], "flasg":{}}

        if self.version:
            json_info["version"] = self.version
        if self.image_width:
            json_info["imageWidth"] = self.image_width
        if self.image_height:
            json_info["imageHeight"] = self.image_height
        if self.img_name:
            json_info["imagePath"] = self.img_name
        if self.flags:
            json_info["flags"] = self.flags
        #
        for each_shape in self._alarms:
            each_shape_info = {
                "label": each_shape.tag,
                "points": [[each_shape.x, each_shape.y]],
                "group_id": each_shape.group_id,
                "shape_type": each_shape.shape_type}
            json_info["shapes"].append(each_shape_info)

        # save img data
        if self.img_path and include_img_data:
            img = cv2.imdecode(np.fromfile(self.img_path, dtype=np.uint8), 1)
            image_data_bs64 = utils.img_arr_to_b64(img).decode('utf-8')
            json_info["imageData"] = image_data_bs64

        # save
        JsonUtil.save_data_to_json_file(json_info, save_json_path, encoding="GBK")

    def save_to_json_str(self):
        pass

    def draw_res(self):
        pass

    def print_as_fzc_format(self):
        pass

    def add_obj(self):
        pass

    def add_obj_2(self, point_obj):
        self.alarms.append(point_obj)

    def deep_copy(self, copy_img=False):

        if copy_img:
            return copy.deepcopy(self)
        else:
            a = DeteRes()
            a.parse_auto = False
            a.height = self.height
            a.width = self.width
            a.json_path = self.json_path
            a.img_path = self.img_path
            a.file_name = self.file_name
            a.folder = self.folder
            # img 是不进行深拷贝的，因为不会花很长的时间
            a.img = self.img
            a.json_dict = copy.deepcopy(self.json_dict)
            a.reset_alarms(copy.deepcopy(self.alarms))
            a.redis_conn_info = self.redis_conn_info
            a.img_redis_key = self.img_redis_key
            a.parse_auto = True
            return a

    def del_point_obj(self, assign_dete_obj):
        #
        for each_point_obj in copy.deepcopy(self._alarms):
            if each_point_obj == assign_dete_obj:
                # del each_dete_obj # 使用 del 删除不了
                self._alarms.remove(each_point_obj)
                # break or not
                if not del_all:
                    return

    def filter_by_tags(self, tags):

        if tags:
            res = self.deep_copy()
            for each_point_obj in PointRes:
                if each_point_obj.tag in tags:
                    res.add_obj_2(each_point_obj)
            return res









