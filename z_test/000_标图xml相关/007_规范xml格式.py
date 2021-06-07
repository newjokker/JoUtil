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



xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\999_wait_for_train\武汉电科院_2021_04\img"


for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):

    a = DeteRes(each_xml_path)
    a.save_to_xml(each_xml_path)