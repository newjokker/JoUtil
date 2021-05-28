# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
import shutil
import cv2
import PIL.Image as Image
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil

xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\999_wait_for_train\武汉电科院_2021_05\xml"
img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\999_wait_for_train\武汉电科院_2021_05\img"
save_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\999_wait_for_train\武汉电科院_2021_05\crop_01"


OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True, augment_parameter=[0.1, 0.1, 0.1, 0.1])


# a = cv2.imread(r"C:\Users\14271\Desktop\del\png\202104_353173.jpg")
# print(a.shape)

# b = Image.open(r"C:\Users\14271\Desktop\del\img\110kV德七Ⅰ回_0塔头 (1).jpg")
# print(b.mode)
#
# # 将一个4通道转化为rgb三通道
# b = b.convert("RGB")

# a = DeteRes()
# a.update_tags({"key_1":"key", "key_2":"key"})


# OperateDeteRes.get_xml_from_crop_xml(xml_dir, img_dir, save_xml_dir)

# OperateDeteRes.get_xml_from_crop_img(crop_dir, region_img_dir=img_dir, save_xml_dir=save_dir)


# for each in OperateDeteRes.get_class_count(save_dir).items():
#     print(each)
#
#
# for each in FileOperationUtil.re_all_file(r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\JPEGImages"):
#     img_name = os.path.split(each)[1]
#     xml_name = img_name[:-3] + 'xml'
#     xml_path = os.path.join(r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\Annotations_broken", xml_name)
#
#     if not os.path.exists(xml_path):
#         print(each)


