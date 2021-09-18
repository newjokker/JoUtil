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



xml_dir = r"\\192.168.3.80\算法\绝缘子数据\Annotations"
img_dir = r"\\192.168.3.80\算法\绝缘子数据\JPEGImages"
save_dir = r"E:\jyz_leiji_niaofen"


# OperateDeteRes.get_class_count(xml_dir, print_count=True)

new_img_dir = os.path.join(save_dir, "JPEGImages")
new_xml_dir = os.path.join(save_dir, "Annotations")
os.makedirs(new_img_dir, exist_ok=True)
os.makedirs(new_xml_dir, exist_ok=True)


index = 0
for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):
    # each_img_path = os.path.join(img_dir, FileOperationUtil.bang_path(each_xml_path)[1] + '.jpg')
    each_img_path = OperateDeteRes.get_assign_file_path(FileOperationUtil.bang_path(each_xml_path)[1], img_dir, suffix_list=('.jpg', '.JPG'))
    #

    print(index, each_xml_path)
    index += 1

    if each_xml_path:

        a = DeteRes(each_xml_path)

        if a.has_tag('ps'):

            new_img_path = os.path.join(new_img_dir, os.path.split(each_img_path)[1])
            new_xml_path = os.path.join(new_xml_dir, os.path.split(each_xml_path)[1])

            shutil.copy(each_img_path, new_img_path)
            shutil.copy(each_xml_path, new_xml_path)
