# -*- coding: utf-8  -*-
# -*- author: jokker -*-



import os
from ReadData.JsonUtil import JsonUtil


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
        self.id = json_info["id"]
        self.name = json_info["name"]
        self.size = json_info["size"]
        self.btime = json_info["btime"]
        self.mtime = json_info["mtime"]
        self.ext = json_info["ext"]         # 后缀
        self.tags = json_info["tags"]          # 标签
        self.folders = json_info["folders"]
        self.is_deleted = json_info["isDeleted"]
        self.url = json_info["url"]
        self.annotation = json_info["annotation"]
        self.modification_time = json_info["modificationTime"]
        self.height = json_info["height"]
        self.width = json_info["width"]
        self.orientation = json_info["orientation"]
        self.last_modified = json_info["lastModified"]
        self.palettes = json_info["palettes"]                # 应该是色板，记录了图中最常出现的几种颜色和比例

    def add_tags(self, tag):
        """增加标签"""
        self.tags.append(tag)

    def save_to_json_file(self, file_path):
        """保存属性为 json 文件"""
        json_info = {
                        "id": self.id,
                        "name": self.name,
                        "size":self.size,
                        "btime":self.btime,
                        "mtime":self.mtime,
                        "ext":self.ext,      # 后缀
                        "tags":self.tags,          # 标签
                        "folders":self.folders,
                        "is_deleted":self.is_deleted,
                        "url":self.url,
                        "annotation":self.annotation,
                        "modification_time":self.modification_time,
                        "height":self.height,
                        "width":self.width,
                        "orientation":self.orientation,
                        "last_modified":self.last_modified,
                        "palettes":self.palettes
        }
        JsonUtil.save_data_to_json_file(json_info, file_path)


class EagleUtil(object):
    """处理使用标图工具 eagle 的类"""

    @staticmethod
    def read_meta_data(json_path):
        """读取 json 原数据"""
        eagle_meta_data = EagleMetaData()
        eagle_meta_data.load_atts_from_json(json_path)
        return eagle_meta_data



if __name__ == "__main__":


    a = EagleUtil.read_meta_data(r"C:\data\edgle\FZC.library\images\KDH5EVWARA22B.info\metadata.json")

    print(a)

    pass



