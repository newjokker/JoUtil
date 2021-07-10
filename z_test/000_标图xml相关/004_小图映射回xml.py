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


img_dir = r"C:\Users\14271\Desktop\寻找未被发现的fzc_broken\JPEGImages"
crop_dir = r"C:\Users\14271\Desktop\寻找未被发现的fzc_broken\crop"
xml_dir = r"C:\Users\14271\Desktop\寻找未被发现的fzc_broken\xml"


OperateDeteRes.get_xml_from_crop_img(region_img_dir=img_dir, crop_dir=crop_dir, save_xml_dir=xml_dir)

OperateDeteRes.get_class_count(xml_dir, print_count=True)

