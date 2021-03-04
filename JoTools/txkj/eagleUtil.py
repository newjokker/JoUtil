# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import time
import os
import copy
import random
import shutil
from PIL import Image
from JoTools.utils.HashlibUtil import HashLibUtil
from JoTools.utils.JsonUtil import JsonUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil

# todo 其中的 ID 是如何生成的，是不是有一定的规范，还是说就是随机的，
    # KDH5E VWAR A22B 13 位数字和大写字母组成，应该是随机的
    # KDH5E VWB0 7AGW

# todo 一组图片自动生成 eagle 的元数据

# todo 将有标签的数据自动导入 edgal 信息中，读取 img 和 xml 自动在 edgal 中打标签

# todo 最外面的源文件存放的是文件夹的等级信息，这个需要进行模仿

# todo 完善主动生成 ID 的唯一性
# todo 完善


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
            self.time_dict[assign_id] = new_time
            # raise ValueError("assign id not in time_dict")

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


class EagleFolderMetaData(object):

    def __init__(self):
        self.applicationVersion = "2.0.0"
        self.folders = []
        self.smartFolders = []
        self.quickAccess = []
        self.tagsGroups = []
        self.modificationTime = int(time.time()*1000)

    def save_to_json_file(self, json_path):
        json_info = {"applicationVersion":self.applicationVersion, "folders":self.folders, "smartFolders":self.smartFolders,
                     "quickAccess":self.quickAccess, "tagsGroups":self.tagsGroups, "modificationTime":self.modificationTime}
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

    def __init__(self):
        self.proj_dir = r""
        self.id_set = {}

    @staticmethod
    def get_tag_dict(img_dir):
        """合并图像信息，拿到每个图像对应的标签"""
        tag_dict, md5_dict = {}, {}
        for each_img_path in FileOperationUtil.re_all_file(img_dir, lambda x:str(x).endswith((".jpg", ".JPG"))):
            dir_name = os.path.dirname(each_img_path)
            dir_name_2 = os.path.dirname(dir_name)
            # get md5, tag
            each_tag = dir_name[len(dir_name_2)+1:]
            each_md5 = HashLibUtil.get_file_md5(each_img_path)
            #
            if each_md5 in md5_dict:
                old_img_path = md5_dict[each_md5]
                tag_dict[old_img_path].add(each_tag)
            else:
                md5_dict[each_md5] = each_img_path
                tag_dict[each_img_path] = {each_tag}
        return tag_dict

    def get_id_name_dict(self):
        """获取 id 和 name 对应的字典"""
        name_dict = {}
        image_dir = os.path.join(self.proj_dir, "images")
        for each_json_path in FileOperationUtil.re_all_file(image_dir, lambda x:str(x).endswith("metadata.json")):
            a = EagleMetaData()
            a.load_atts_from_json(each_json_path)
            name_dict[a.name] = a.id
        return name_dict

    @staticmethod
    def get_modification_time():
        return int(time.time()*1000)

    def get_random_id(self):
        """随机获取图片的 id"""
        while True:
            random_id = "KDH5" + str(random.randint(100000000, 1000000000))
            if random_id not in self.id_set:
                return random_id

    def init_edgal_project(self, img_dir):
        """初始化一个 edgal 工程"""

        tag_json_path = os.path.join(self.proj_dir, "tags.json")
        mtime_json_path = os.path.join(self.proj_dir, "mtime.json")
        faster_metadata_json_path = os.path.join(self.proj_dir, "metadata.json")

        tag = EagleTags()
        mtime = EagleMTimes()
        tag_dict = EagleOperate.get_tag_dict(img_dir)
        faster_metadata = EagleFolderMetaData()

        # 创建对应的文件夹
        back_up_dir = os.path.join(self.proj_dir, "backup")
        images_dir = os.path.join(self.proj_dir, "images")
        os.makedirs(back_up_dir, exist_ok=True)
        os.makedirs(images_dir, exist_ok=True)
        # 完善 images 文件夹
        for each_img_path in tag_dict:
            a = EagleMetaData()
            each_mo_time = EagleOperate.get_modification_time()
            each_id = self.get_random_id()
            #
            for each_tag in tag_dict[each_img_path]:
                a.add_tags(each_tag)
                tag.add_tags(each_tag)
            mtime.update_assign_id(each_id, each_mo_time)
            #
            img = Image.open(each_img_path)
            a.modification_time = each_mo_time
            a.id = each_id
            a.name = FileOperationUtil.bang_path(each_img_path)[1]
            a.width = img.width
            a.height = img.height
            a.mtime = each_mo_time
            a.btime = each_mo_time
            a.folders = []
            a.ext = each_img_path[-3:]
            a.size = os.path.getsize(each_img_path)
            #
            each_img_dir = os.path.join(self.proj_dir, "images", each_id + '.info')
            save_img_path = os.path.join(each_img_dir, os.path.split(each_img_path)[1])
            os.makedirs(each_img_dir, exist_ok=True)

            shutil.copy(each_img_path, save_img_path)

            each_meta_json_path =  os.path.join(each_img_dir, "metadata.json")
            a.save_to_json_file(each_meta_json_path)

        tag.save_to_json_file(tag_json_path)
        mtime.save_to_json_file(mtime_json_path)
        faster_metadata.save_to_json_file(faster_metadata_json_path)



if __name__ == "__main__":

    # todo 三步走 （1）计算文件的重复字典（2）文件去重导入 edgal （3）根据重复字典修改edgal文件中的元数据
    # fixme 注意的是文件名需要是唯一的，不能重复，否则就不存在一一对应的关系


    a = EagleOperate()
    a.proj_dir = r"C:\Users\14271\Desktop\del\hehe_021.library"

    # a.get_id_name_dict()


    img_dir = r"C:\Users\14271\Desktop\del\test"

    a.init_edgal_project(img_dir)





