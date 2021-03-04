# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import time
import os
import copy
from JoTools.utils.JsonUtil import JsonUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil


class EagleMetaData(object):
    """Eagle 元数据"""

    def __init__(self):
        self.id = None
        self.name = None
        self.size = None
        self.btime = None
        self.mtime = None
        self.ext = None         # 后缀
        self.tags = []          # 标签
        self.folders = []
        self.is_deleted = None
        self.url = None
        self.annotation = None
        self.modification_time = None
        self.height = None
        self.width = None
        self.orientation = None
        self.last_modified = None
        self.palettes = None                # 应该是色板，记录了图中最常出现的几种颜色和比例

        self.attrs = ["id", "name", "size", "btime", "mtime", "ext", "tags", "folders", "isDeleted",
                      "url", "annotation", "modificationTime", "height", "width", "orientation", "lastModified", "palettes"]

    def load_atts_from_json(self, json_path):
        """从 json 中获取属性"""
        json_info = JsonUtil.load_data_from_json_file(json_path)
        # 赋值属性
        for each_attr in self.attrs:
            if each_attr in json_info:
                setattr(self, each_attr, json_info[each_attr])

    def add_tags(self, tag):
        """增加标签"""
        self.tags.append(tag)

    def save_to_json_file(self, file_path):
        """保存属性为 json 文件"""
        json_info = {}

        for each_attr in self.attrs:
            # 存在属性
            if hasattr(self, each_attr):
                # 不是 None 默认值
                if getattr(self, each_attr) is not None:
                    json_info[each_attr] = getattr(self, each_attr)

        JsonUtil.save_data_to_json_file(json_info, file_path)


class EagleMTimes(object):

    def __init__(self):
        self.time_dict = {}

    def load_from_json(self, json_path):
        """从json中读取数据"""
        self.time_dict = JsonUtil.load_data_from_json_file(json_path)
        del self.time_dict["all"]

    def update_assign_id(self, assign_id, new_time):
        """更新指定id的时间"""
        if assign_id in self.time_dict:
            self.time_dict[assign_id] = new_time
        else:
            raise ValueError("assign id not in time_dict")

    def save_to_json_file(self, save_path):
        """保存为 json 文件"""
        json_info = copy.deepcopy(self.time_dict)
        json_info["all"] = len(self.time_dict)
        JsonUtil.save_data_to_json_file(json_info, save_path)


class EagleTags(object):

    def __init__(self):
        self.historyTags = set()
        self.starredTags = set()

    def load_from_json(self, json_path):
        json_info = JsonUtil.load_data_from_json_file(json_path)
        self.historyTags = set(json_info["historyTags"])
        self.starredTags = set(json_info["starredTags"])

    def add_tags(self, tag):
        """更新指定id的时间"""
        self.historyTags.add(tag)

    def save_to_json_file(self, json_path):
        json_info = {"historyTags":list(self.historyTags), "starredTags":list(self.starredTags)}
        JsonUtil.save_data_to_json_file(json_info, json_path)


class EagleUtil(object):
    """处理使用标图工具 eagle 的类"""

    @staticmethod
    def read_meta_data(json_path):
        """读取 json 原数据"""
        eagle_meta_data = EagleMetaData()
        eagle_meta_data.load_atts_from_json(json_path)
        return eagle_meta_data

    @staticmethod
    def add_tags():
        """123"""


        tag_json_path = r"C:\data\edgle\FZCTEST.library\tags.json"
        mtime_json_path = r"C:\data\edgle\FZCTEST.library\mtime.json"
        meta_json_path = r"C:\data\edgle\FZCTEST.library\images\KDH5EVWARA22B.info\metadata.json"

        tags = EagleTags()
        tags.load_from_json(tag_json_path)

        mtime = EagleMTimes()
        mtime.load_from_json(mtime_json_path)

        meta_data = EagleMetaData()
        meta_data.load_atts_from_json(meta_json_path)

        # 增加 tags
        new_tag = "test_new"
        meta_data.add_tags(new_tag)
        assign_id = meta_data.id
        new_time = int(time.time() * 1000)
        meta_data.modification_time = new_time
        mtime.update_assign_id(assign_id, new_time)
        tags.add_tags(new_tag)

        meta_data.save_to_json_file(meta_json_path)
        mtime.save_to_json_file(mtime_json_path)
        tags.save_to_json_file(tag_json_path)


class EagleOperate(object):

    # todo 一组图片自动生成 eagle 的元数据

    # todo 将有标签的数据自动导入 edgal 信息中，读取 img 和 xml 自动在 edgal 中打标签

    @staticmethod
    def merge_img_info(img_dir):
        """合并图像信息，拿到每个图像对应的标签"""




if __name__ == "__main__":

    img_dir = r"C:\Users\14271\Desktop\del\test"





