# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import shutil
import os
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.JsonUtil import JsonUtil

# img_dir = r"D:\data\001_fzc_优化相关资料\dataset_fzc\000_0_标准测试集\JPEGImages"
# xml_dir = r"D:\data\001_fzc_优化相关资料\dataset_fzc\000_0_标准测试集\Annotations"
# save_dir = r"C:\Users\14271\Desktop\img_dir"
#
#
# jpg_list = []
#
#
# for each_xml_path in FileOperationUtil.re_all_file(xml_dir,endswitch=['.xml']):
#
#     each_xml_name = FileOperationUtil.bang_path(each_xml_path)[1]
#
#     each_img_path = os.path.join(img_dir, each_xml_name + '.jpg')
#
#     a = DeteRes(each_xml_path)
#
#     if a.has_tag("fzc_broken"):
#         jpg_list.append(each_img_path)
#
#
# FileOperationUtil.move_file_to_folder(jpg_list, save_dir)


img_dir = r"C:\Users\14271\Desktop\input_dir"

json_info = []

index = 0

for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg']):
    index += 1
    each_img_name = os.path.split(each_img_path)[1]

    json_info.append({
        "originFileName":each_img_name,
        "fileName":"chinese_name" + each_img_name,
    })

JsonUtil.save_data_to_json_file(json_info, r"C:\Users\14271\Desktop\input_dir.json")


    # new_img_path = os.path.join(os.path.split(each_img_path)[0], str(index) + '.jpg')
    #
    # index += 1
    #
    # shutil.move(each_img_path, new_img_path)
    #























