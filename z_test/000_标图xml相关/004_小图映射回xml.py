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


img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\999_wait_for_train\武汉电科院四月五月数据\img_xml"
xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\999_wait_for_train\武汉电科院四月五月数据\xml_new"
crop_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\999_wait_for_train\武汉电科院四月五月数据\crop_fix_by_ldq"


OperateDeteRes.get_xml_from_crop_img(region_img_dir=img_dir, img_dir=crop_dir, save_xml_dir=xml_dir)


for each in OperateDeteRes.get_class_count(xml_dir).items():
    print(each)

