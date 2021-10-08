# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import cv2
import numpy as np
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes, DeteObj


# xml_dir = r"D:\data\001_fzc_优化相关资料\dataset_fzc\000_train_data_step_1\Annotations"
# img_dir = r"D:\data\001_fzc_优化相关资料\dataset_fzc\000_train_data_step_1\JPEGImages"

xml_dir = r"D:\data\004_绝缘子污秽\000_定位数据\Annotations"
img_dir = r"D:\data\004_绝缘子污秽\000_定位数据\JPEGImages"

width = 300
height = 300

canvas = np.ones((width, height, 3), dtype="uint8")

for index, each_xml_path in enumerate(FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml'])):
    each_img_path = os.path.join(img_dir, FileOperationUtil.bang_path(each_xml_path)[1] + '.jpg')
    a = DeteRes(each_xml_path, assign_img_path=each_img_path)
    print(index, each_xml_path)
    for each_dete_obj in a:
        if isinstance(each_dete_obj, DeteObj):
            each_point = [(each_dete_obj.x1 + each_dete_obj.x2) / (a.width * 2), (each_dete_obj.y1 + each_dete_obj.y2) / (a.height * 2)]
            canvas[int(width * each_point[0]), int(height * each_point[1]), :] += 1

cv2.imwrite(r"C:\Users\14271\Desktop\jyz.jpg", canvas*50)

















