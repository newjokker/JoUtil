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

# img_dir = r"C:\Users\14271\Desktop\寻找未被发现的fzc_broken\JPEGImages"
# xml_dir = r"C:\Users\14271\Desktop\寻找未被发现的fzc_broken\Annotations"
# save_dir = r"C:\Users\14271\Desktop\寻找未被发现的fzc_broken\crop"

# img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\JPEGImages"
# xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\Annotations"
# save_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\001_train_data_step_1.5\fzc_v0.2.5.x_classify\crop"

img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_0_标准测试集\JPEGImages"
xml_dir = r"C:\Users\14271\Desktop\fzc_v1.2.5.0_new版本\001_dete_res\fzc_v1.2.5.4-B_new\compare_xml"
save_dir = r"C:\Users\14271\Desktop\fzc_v1.2.5.0_new版本\001_dete_res\fzc_v1.2.5.4-B_new\crop"


# OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True, augment_parameter=[0.3, 0.3, 0.3, 0.3], exclude_tag_list=['correct_fzc'])
# OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True, augment_parameter=[0.3, 0.3, 0.3, 0.3])
OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True, exclude_tag_list=["correct_Fnormal", "miss_Fnormal"])
# OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True, augment_parameter=[0.3, 0.3, 0.3, 0.3])


