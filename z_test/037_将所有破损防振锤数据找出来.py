# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
import shutil
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkj.eagleUtil import EagleMetaData, EagleOperate
from JoTools.operateDeteRes import OperateDeteRes

img_dir = r"/home/suanfa-1/武汉/2021年4月集中培育/金具/保护金具/防振锤"
xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\999_wait_for_train\武汉电科院_2021_04\xml"
save_dir = r"/home/suanfa-4/ldq/del/broken_img"

index = 0
for each_xml_path in FileOperationUtil.re_all_file(xml_dir, lambda x:str(x).endswith(".xml")):

    a = DeteRes(xml_path=each_xml_path)
    a.save_to_xml(each_xml_path)

    # img_path = os.path.join(img_dir, os.path.split(each_xml_path)[1][:-3] + 'jpg')
    # save_img_path = os.path.join(save_dir, os.path.split(each_xml_path)[1][:-3] + 'jpg')
    # save_xml_path = os.path.join(save_dir, os.path.split(each_xml_path)[1])
    # if os.path.exists(img_path):
    #     each_dete_res = DeteRes(each_xml_path)
    #     if each_dete_res.has_tag("040303021"):
    #         shutil.copy(img_path, save_img_path)
    #         shutil.copy(each_xml_path, save_xml_path)
    #         index += 1
    #         print(index, each_xml_path)
    #




