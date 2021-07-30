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


json_dir = r"C:\data\004_绝缘子污秽\002_测试标图流程\json"
save_dir = r"C:\data\004_绝缘子污秽\002_测试标图流程\crop_box"

index = 1
for each_json_path in FileOperationUtil.re_all_file(json_dir, endswitch=['.json']):
    a = SegmentRes()
    a.parse_json_info(json_path=each_json_path, parse_mask=True, parse_img=True)
    a.crop_and_save(save_dir)
    print(index, each_json_path)
    index += 1




