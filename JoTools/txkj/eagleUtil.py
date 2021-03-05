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
from JoTools.txkjRes.deteRes import DeteRes

# todo 将有标签的数据自动导入 edgal 信息中，读取 img 和 xml 自动在 edgal 中打标签
# todo 最外面的源文件存放的是文件夹的等级信息，这个需要进行模仿
# todo 顺便生成压缩文件（png格式）
# todo xml 信息直接以 json_str 的格式存入图片中
# todo 多个 edgal 项目进行合并
# todo 将 edgal 图片按照一定的规则进行导出
# todo 给一个项目地址，先完成项目的初始化，如果有文件的话先去读取指定的文件
# todo 看看 edgal 里面是否可以标图，可以的话是怎么标注的，是不是写在源文件中的，尝试增加标注, eagel 中的标注和 labelImg 中的标注互联互通
# todo edgal 中的图像和标注转为标准格式的（img, xml）
# fixme 可以主动选择分析颜色，选中需要的图片，右击更多，重新分析颜色


class EagleMetaData(object):
    """Eagle 元数据"""

    def __init__(self):
        self.id = None
        self.name = None
        self.size = None
        self.btime = None
        self.mtime = None
        self.ext = None                     # 后缀
        self.tags = []                      # 标签
        self.folders = []
        self.is_deleted = None
        self.url = None
        self.annotation = None
        self.modification_time = None       # 注释
        self.height = None
        self.width = None
        self.orientation = None
        self.last_modified = None
        self.palettes = None                # 应该是色板，记录了图中最常出现的几种颜色和比例
        self.comments = None                # 标注
        #
        self.attrs = ["id", "name", "size", "btime", "mtime", "ext", "tags", "folders", "isDeleted",
                      "url", "annotation", "modificationTime", "height", "width", "orientation", "lastModified", "palettes", "comments"]

    def load_atts_from_json(self, json_path):
        """从 json 中获取属性"""
        json_info = JsonUtil.load_data_from_json_file(json_path)
        # 赋值属性
        for each_attr in self.attrs:
            if each_attr in json_info:
                setattr(self, each_attr, json_info[each_attr])

    def add_tag(self, tag):
        """增加标签"""
        if tag not in self.tags:
            self.tags.append(tag)

    def add_comment(self, x1, y1, x2, y2, annotation, assign_id, last_modified):
        """添加标注框"""
        comment_info = {"id":assign_id, "x":x1, "y":y1, "width":x2-x1, "height":y2-y1, "annotation":annotation, "lastModified":last_modified}
        if self.comments is None:
            self.comments = [comment_info]
        else:
            self.comments.append(comment_info)

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


class EagleOperate(object):

    def __init__(self, proj_dir, img_dir):

        os.makedirs(proj_dir, exist_ok=True)
        self.proj_dir = proj_dir
        self.id_set = set()
        self.tag_dict = {}
        self.md5_dict = {}
        self.img_dir = img_dir
        #
        self.tag_json_path = os.path.join(self.proj_dir, "tags.json")
        self.mtime_json_path = os.path.join(self.proj_dir, "mtime.json")
        self.faster_metadata_json_path = os.path.join(self.proj_dir, "metadata.json")
        self.back_up_dir = os.path.join(self.proj_dir, "backup")
        self.images_dir = os.path.join(self.proj_dir, "images")

    @staticmethod
    def get_modification_time():
        return int(time.time()*1000)

    @staticmethod
    def get_thumbnail_img(img_path, save_path, min_length=300):
        """获取并保存缩略图"""
        img = Image.open(img_path)
        if img.width > min_length and img.height > min_length:
            scale = min(img.width/min_length, img.height/min_length)
            thumbnail = img.resize((int(img.width/scale), int(img.height/scale)))
            thumbnail.save(save_path)
        else:
            img.save(save_path)

    @staticmethod
    def json_to_xml(json_path, xml_dir):
        """将 metadata json 文件转为 xml 文件"""
        a = EagleMetaData()
        a.load_atts_from_json(json_path)
        # 读取 comment 中的信息，并直接转为 xml 信息
        b = DeteRes()
        for each_comment in a.comments:
            print(each_comment)
            x1 = int(each_comment["x"])
            y1 = int(each_comment["y"])
            x2 = int(each_comment["x"] + each_comment["width"])
            y2 = int(each_comment["y"] + each_comment["height"])
            tag = str(each_comment["annotation"])
            b.add_obj(x1, y1, x2, y2, tag, conf=-1)
        #
        b.width = a.width
        b.height = a.height
        save_xml_path = os.path.join(xml_dir, a.name + '.xml')
        b.save_to_xml(save_xml_path)

    def get_random_id(self):
        """随机获取图片的 id"""
        while True:
            random_id = "KDH5" + str(random.randint(100000000, 1000000000))
            if random_id not in self.id_set:
                self.id_set.add(random_id)
                return random_id

    def get_tag_dict(self, img_dir):
        """合并图像信息，拿到每个图像对应的标签"""
        # tag_dict, md5_dict = {}, {}
        for img_index, each_img_path in enumerate(FileOperationUtil.re_all_file(img_dir, lambda x:str(x).endswith((".jpg", ".JPG")))[:500]):
            print(img_index, "get md5 info", each_img_path)
            dir_name = os.path.dirname(each_img_path)
            # get md5, tag
            each_tags = set(dir_name[len(self.img_dir)+1:].split(os.sep))
            # dir_name_2 = os.path.dirname(dir_name)
            # each_tags = dir_name[len(dir_name_2)+1:]
            each_md5 = HashLibUtil.get_file_md5(each_img_path)
            #
            if each_md5 in self.md5_dict:
                old_img_path = self.md5_dict[each_md5]
                self.tag_dict[old_img_path].update(each_tags)
            else:
                self.md5_dict[each_md5] = each_img_path
                self.tag_dict[each_img_path] = each_tags
        # return tag_dict

    def get_id_name_dict(self):
        """获取 id 和 name 对应的字典"""
        name_dict = {}
        image_dir = os.path.join(self.proj_dir, "images")
        for each_json_path in FileOperationUtil.re_all_file(image_dir, lambda x:str(x).endswith("metadata.json")):
            a = EagleMetaData()
            a.load_atts_from_json(each_json_path)
            name_dict[a.name] = a.id
        return name_dict

    def init_edgal_project(self, img_dir):
        """初始化一个 edgal 工程"""
        tag = EagleTags()
        mtime = EagleMTimes()
        self.get_tag_dict(img_dir)
        faster_metadata = EagleFolderMetaData()
        # 创建对应的文件夹
        os.makedirs(self.back_up_dir, exist_ok=True)
        os.makedirs(self.images_dir, exist_ok=True)
        # 完善 images 文件夹
        index = 0
        for each_img_path in self.tag_dict:
            a = EagleMetaData()
            each_mo_time = EagleOperate.get_modification_time()
            each_id = self.get_random_id()
            # ----------------------------------------------------------------------------
            # 添加 tag 信息
            for each_tag in self.tag_dict[each_img_path]:
                a.add_tag(each_tag)
                tag.add_tags(each_tag)
            # ----------------------------------------------------------------------------
            # 添加标注信息
            each_dir, each_img_name, _ = FileOperationUtil.bang_path(each_img_path)
            each_xml_path = os.path.join(each_dir, "xml", each_img_name + '.xml')
            if os.path.exists(each_xml_path):
                each_dete_res = DeteRes(xml_path=each_xml_path)
                for each_dete_obj in each_dete_res.alarms:
                    a.add_comment(each_dete_obj.x1, each_dete_obj.y1, each_dete_obj.x2, each_dete_obj.y2, each_dete_obj.tag, self.get_random_id(), EagleOperate.get_modification_time())
            # ----------------------------------------------------------------------------
            # 完善属性
            mtime.update_assign_id(each_id, each_mo_time)
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
            each_save_name = FileOperationUtil.bang_path(each_img_path)[1]
            save_img_path = os.path.join(each_img_dir, each_save_name + '.jpg')
            save_img_thumbnail_path = os.path.join(each_img_dir, each_save_name + "_thumbnail.png")
            os.makedirs(each_img_dir, exist_ok=True)
            # 拷贝文件，生成缩略图
            index += 1
            shutil.copy(each_img_path, save_img_path)
            EagleOperate.get_thumbnail_img(each_img_path, save_img_thumbnail_path)
            #
            print("move :", index, each_img_path)
            each_meta_json_path =  os.path.join(each_img_dir, "metadata.json")
            a.save_to_json_file(each_meta_json_path)

        tag.save_to_json_file(self.tag_json_path)
        mtime.save_to_json_file(self.mtime_json_path)
        faster_metadata.save_to_json_file(self.faster_metadata_json_path)

    def save_to_xml_img(self, save_dir):
        """直接转为我们常用的数据集"""

        # todo 如何解决文件名重复的问题，如何重建文件夹结构？

        # Annotations, JPEGImages
        xml_dir = os.path.join(save_dir, "Annotations")
        img_dir = os.path.join(save_dir, "JPEGImages")
        os.makedirs(xml_dir, exist_ok=True)
        os.makedirs(img_dir, exist_ok=True)
        #
        for each_metadata_path in FileOperationUtil.re_all_file(self.images_dir, lambda x:str(x).endswith(".json")):
            # 解析 json 文件
            EagleOperate.json_to_xml(each_metadata_path, xml_dir)
            # 复制 jpg 文件
            each_img_path = FileOperationUtil.re_all_file(os.path.dirname(each_metadata_path), lambda x:str(x).endswith((".jpg", ".JPG")))[0]
            each_save_img_path = os.path.join(img_dir, os.path.split(each_img_path)[1])
            shutil.copy(each_img_path, each_save_img_path)


if __name__ == "__main__":

    imgDir = r"C:\Users\14271\Desktop\del\test"
    # imgDir = r"D:\算法培育-6月样本"

    a = EagleOperate(r"C:\Users\14271\Desktop\del\test_new_tag.library", imgDir)

    # a.init_edgal_project(imgDir)

    a.save_to_xml_img(r"C:\Users\14271\Desktop\del\new_res")





