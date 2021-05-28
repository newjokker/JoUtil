# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.operateDeteRes import OperateDeteRes

img_dir = r"D:\fzc\img"
xml_dir = r"D:\fzc\xml"



# for each in OperateDeteRes.get_class_count(xml_dir).items():
#     print(each)
#
# exit()


copy_file_list = []
for each_xml_path in FileOperationUtil.re_all_file(xml_dir,endswitch=['.xml']):
    each_img_path = os.path.join(img_dir, os.path.split(each_xml_path)[1][:-3]+'jpg')

    a = DeteRes(each_xml_path)

    if a.has_tag("040303021") or a.has_tag("040303022"):
        if os.path.exists(each_img_path) and os.path.exists(each_xml_path):
            copy_file_list.append(each_xml_path)
            copy_file_list.append(each_img_path)
        else:
            print("* error : {0}".format(each_xml_path))

FileOperationUtil.move_file_to_folder(copy_file_list, r"C:\data\fzc_优化相关资料\dataset_fzc\999_wait_for_train\武汉电科院_2021_05")










