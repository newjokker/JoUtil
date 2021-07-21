# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes,DeteObj
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.RandomUtil import RandomUtil


img_dir = r"/home/suanfa-5/ldq/002_test_data/69G塔基"
xml_dir = r"/home/ldq/tj_dete/merge_new"
save_dir = r"/home/ldq/tj_dete/train_data"

img_save_dir = os.path.join(save_dir, "JPEGImages")
xml_save_dir = os.path.join(save_dir, "Annotations")

os.makedirs(img_save_dir, exist_ok=True)
os.makedirs(xml_save_dir, exist_ok=True)

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

    # a.filter_by_area(50*100)

    if len(a) < 1:
        continue

    img_path_list.append(each_img_path)
    xml_path_list.append(each_xml_path)

FileOperationUtil.move_file_to_folder(img_path_list, img_save_dir, is_clicp=False)
FileOperationUtil.move_file_to_folder(xml_path_list, xml_save_dir, is_clicp=False)



