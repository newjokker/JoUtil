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

# up_dict = {
#     "fzc_yt": "fzc",
#     "fzc_sm": "fzc",
#     "fzc_gt": "fzc",
#     "zd_yt": "fzc",
#     "zd_sm": "fzc",
#     "zd_gt": "fzc",
#     "qx_yt": "fzc",
#     "qx_sm": "fzc",
#     "qx_gt": "fzc",
#     "fzc_other": "fzc",
#     "fzc_broken": "fzc",
#     "other": "other"}

up_dict = {"Fnormal": "fzc", "fzc_broken":"fzc"}

xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_0_标准测试集\xml"
save_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_0_标准测试集\xml_one"

for each in OperateDeteRes.get_class_count(xml_dir).items():
    print(each)

print('-'*50)

for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):
    a = DeteRes(each_xml_path)
    a.update_tags(up_dict)
    # a.filter_by_tags(need_tag=["fzc"])
    save_path = os.path.join(save_dir, os.path.split(each_xml_path)[1])
    a.save_to_xml(save_path)

for each in OperateDeteRes.get_class_count(save_dir).items():
    print(each)


