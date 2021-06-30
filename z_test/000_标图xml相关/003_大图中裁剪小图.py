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


xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\fix_obj_range\fix_xml"
img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\JPEGImages"
save_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\fix_obj_range\check_crop"

# OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True, augment_parameter=[0.3, 0.3, 0.3, 0.3], exclude_tag_list=['correct_fzc'])
OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True)


