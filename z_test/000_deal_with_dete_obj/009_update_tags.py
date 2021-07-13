# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import random
import os
import shutil
import cv2
import PIL.Image as Image
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes,DeteObj
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.RandomUtil import RandomUtil

up_dict = {
    "fzc_sm": "fzc",
    "fzc_yt": "fzc",
    "fzc_broken": "fzc",
    "fzc_gt": "fzc",
    "zd_yt": "fzc",
    "zd_gt": "fzc",
    "zd_sm": "fzc",
    "qx_yt": "fzc",
    "other1": "fzc",
    "qx_sm": "fzc",
    "K": "fzc",
    "qx_gt": "fzc",
    "XieXingXJ": "fzc",
    "fzc_zhedang": "fzc",
    "other2": "fzc",
    "K2": "fzc",
    "fs": "fzc",
}

# up_dict = {
#     "040500013": "K",
#     "040501013": "螺母锈蚀",
#     "010000023": "nc",
#     "040500023": "kkxTC", # 退出
#     "030100023": "jyzzb",
# }

# up_dict = {"extra": "Fnormal", "UGuaHuan":"Fnormal"}

# up_dict = {"Fnormal": "fzc", "fzc_broken":"fzc"}

xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\Annotations"
save_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\Annotations_one"


OperateDeteRes.get_class_count(xml_dir, print_count=True)

# exit()

for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):
    a = DeteRes(each_xml_path)
    a.update_tags(up_dict)
    # a.filter_by_tags(need_tag=["nc"])
    # a.do_augment(augment_parameter=[0.05,0.05,0.05,0.05])
    save_path = os.path.join(save_dir, os.path.split(each_xml_path)[1])
    a.save_to_xml(save_path)


OperateDeteRes.get_class_count(save_dir, print_count=True)


