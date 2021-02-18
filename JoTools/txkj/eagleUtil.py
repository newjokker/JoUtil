# -*- coding: utf-8  -*-
# -*- author: jokker -*-



import os
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


class EagleUtil(object):
    """处理使用标图工具 eagle 的类"""

    @staticmethod
    def read_meta_data(json_path):
        """读取 json 原数据"""
        eagle_meta_data = EagleMetaData()
        eagle_meta_data.load_atts_from_json(json_path)
        return eagle_meta_data



if __name__ == "__main__":

    # todo 组合条件筛选某一种标签，然后将最后筛选后的结果赋一个标签


    img_dir = r"C:\data\edgle\FZC.library"
    save_dir = r"C:\Users\14271\Desktop\del\img_json"

    for each_file in FileOperationUtil.re_all_file(img_dir, lambda x:str(x).endswith('.json')):

        a = EagleUtil.read_meta_data(each_file)


        if len(a.tags) >= 1:
            print(a.width, a.height, a.name ,a.tags, a.palettes)

            new_save_path = os.path.join(save_dir, a.name+'.json')
            a.save_to_json_file(new_save_path)




