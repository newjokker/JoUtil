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


img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_0_标准测试集\img"
xml_dir = r"C:\Users\14271\Desktop\fzc_v1.2.5.0\test_img_016_extra_xml"
crop_dir = r"C:\Users\14271\Desktop\fzc_v1.2.5.0\test_img_016_extra"


OperateDeteRes.get_xml_from_crop_img(region_img_dir=img_dir, img_dir=crop_dir, save_xml_dir=xml_dir)


for each in OperateDeteRes.get_class_count(xml_dir).items():
    print(each)

