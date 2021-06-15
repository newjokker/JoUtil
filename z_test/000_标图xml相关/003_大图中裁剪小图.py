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


xml_dir = r"C:\Users\14271\Desktop\fzc_多版本对比\xml_v0.2.5.0"
img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_0_标准测试集\img"
save_dir = r"C:\Users\14271\Desktop\fzc_多版本对比\crop_v0.2.4.0"
# OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True, augment_parameter=[0.3, 0.3, 0.3, 0.3], exclude_tag_list=['correct_fzc'])
OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True, augment_parameter=[0.1, 0.1, 0.1, 0.1], exclude_tag_list=['correct_fzc', 'miss_other', 'mistake_other-fzc'])

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



