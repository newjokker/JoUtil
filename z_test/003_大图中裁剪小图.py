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


for i in range(1,4):
    xml_dir = r"\\192.168.3.80\数据\4量化测试集\电科院3月测试集xml\xml修改后\{0}".format(i)
    img_dir = r"\\192.168.3.80\数据\4量化测试集\电科院3月测试集xml\xml修改后\{0}".format(i)
    save_dir = r"C:\Users\14271\Desktop\标准测试集整理"
    OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True, augment_parameter=[0.3,0.3,0.3,0.3])

exit()

# OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True)


index = 0
for each_xml_path in FileOperationUtil.re_all_file(xml_dir, lambda x: str(x).endswith(".xml")):
    each_img_path = os.path.join(img_dir, os.path.split(each_xml_path)[1][:-3] + 'jpg')

    if not os.path.exists(each_img_path):
        continue

    print(index, each_xml_path)
    a = DeteRes(each_xml_path)


    a.img_path = each_img_path
    try:

        augment_parameter = [RandomUtil.rand_range_float(-0.3, 0), RandomUtil.rand_range_float(-0.3, 0), RandomUtil.rand_range_float(-0.2, 0), RandomUtil.rand_range_float(-0.2, 0)]

        print(augment_parameter)

        a.crop_and_save(save_dir, split_by_tag=True, exclude_tag_list=None, augment_parameter=augment_parameter)

        index += 1

    except Exception as e:
        print(e)



