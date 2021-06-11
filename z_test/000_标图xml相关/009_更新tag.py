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
    "fzc_yt": "Fnormal",
    "fzc_sm": "Fnormal",
    "fzc_gt": "Fnormal",
    "zd_yt": "Fnormal",
    "zd_sm": "Fnormal",
    "zd_gt": "Fnormal",
    "qx_yt": "Fnormal",
    "qx_sm": "Fnormal",
    "qx_gt": "Fnormal",
    "fzc_other": "Fnormal",
    "fzc_broken": "Fnormal",
    "other": "other"}

# up_dict = {"extra": "Fnormal", "UGuaHuan":"Fnormal"}

# up_dict = {"Fnormal": "fzc", "fzc_broken":"fzc"}

xml_dir = r"C:\Users\14271\Desktop\updata_step_1_train_data\to_fix_extra_data\Annotations"
save_dir = r"C:\Users\14271\Desktop\updata_step_1_train_data\to_fix_extra_data\Annotations"


OperateDeteRes.get_class_count(xml_dir, print_count=True)


for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):
    a = DeteRes(each_xml_path)
    a.update_tags(up_dict)
    # a.filter_by_tags(need_tag=["fzc"])
    save_path = os.path.join(save_dir, os.path.split(each_xml_path)[1])
    a.save_to_xml(save_path)


OperateDeteRes.get_class_count(save_dir, print_count=True)


