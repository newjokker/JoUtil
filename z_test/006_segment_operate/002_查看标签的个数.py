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


# json_dir = r"C:\data\004_绝缘子污秽\002_测试标图流程\json"
json_dir = r"C:\data\004_绝缘子污秽\001_分割训练数据\train\json"

index = 0
label_num = 0
for each_json_path in FileOperationUtil.re_all_file(json_dir, endswitch=[".json"]):
    print(index, each_json_path)
    a = SegmentRes()
    a.parse_json_info(each_json_path, parse_img=False, parse_mask=False)
    label_num += len(a)
    index += 1

print("label count : {0}".format(label_num))


