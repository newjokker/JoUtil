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



xml_dir = r"C:\Users\14271\Desktop\寻找未被发现的fzc_broken\region_img"


for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):

    a = DeteRes(each_xml_path)
    a.angle_obj_to_obj()
    a.save_to_xml(each_xml_path)
