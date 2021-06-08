# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes,DeteObj
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.RandomUtil import RandomUtil


img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\999_wait_for_train\武汉电科院四月五月数据\img"
xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\999_wait_for_train\武汉电科院四月五月数据\xml_new"
save_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\999_wait_for_train\武汉电科院四月五月数据\train_data"

img_save_dir = os.path.join(save_dir, "JPEGImages")
xml_save_dir = os.path.join(save_dir, "Annotations")

os.makedirs(img_save_dir)
os.makedirs(xml_save_dir)

img_path_list = []
xml_path_list = []

index = 0
for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):

    index += 1
    print(index, each_xml_path)

    xml_name = os.path.split(each_xml_path)[1]
    img_name = xml_name[:-3] + 'jpg'
    each_img_path = os.path.join(img_dir, img_name)

    if not (os.path.exists(each_xml_path) and os.path.exists(each_img_path)):
        print("* 没找到对应的 img 数据： {0}".format(each_img_path))
        continue

    a = DeteRes(each_xml_path)
    if len(a) < 2 and not (a.has_tag("fzc_broken")):
        print("要素过少，或者没有破损数据 ： {0}".format(each_xml_path))
        continue

    img_path_list.append(each_img_path)
    xml_path_list.append(each_xml_path)

FileOperationUtil.move_file_to_folder(img_path_list, img_save_dir, is_clicp=False)
FileOperationUtil.move_file_to_folder(xml_path_list, xml_save_dir, is_clicp=False)



