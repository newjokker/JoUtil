# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.segmentRes import SegmentRes
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil
import base64
import numpy as np
from labelme import utils
import labelme
import cv2
from PIL import Image
import os


img_dir = r"C:\data\004_绝缘子污秽\000_定位数据\z_crop\img"
json_dir = r"C:\data\004_绝缘子污秽\002_测试标图流程\json"
save_dir = r"C:\data\004_绝缘子污秽\002_测试标图流程\img"


copy_list = []
for each_json_path in FileOperationUtil.re_all_file(json_dir, endswitch=[".json"]):
    each_name = FileOperationUtil.bang_path(each_json_path)[1]
    each_img_path = os.path.join(img_dir, each_name + '.jpg')

    if os.path.exists(each_img_path):
        copy_list.append(each_img_path)

FileOperationUtil.move_file_to_folder(copy_list, save_dir, is_clicp=False)