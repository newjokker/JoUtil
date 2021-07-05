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


# fixme 将代码都改为并行的，这样在文件处理操作的时候要快很多！
# fixme 小文件处理并行
# todo 写一个并行的框架，别的函数能很好的直接用进去，或者将方法当做参数传进去

xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\fix_obj_range\xml"
img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\JPEGImages"
save_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\fix_obj_range\crop"

# OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True, augment_parameter=[0.3, 0.3, 0.3, 0.3], exclude_tag_list=['correct_fzc'])
OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True, augment_parameter=[0.2, 0.3, 0.3, 0.3])


