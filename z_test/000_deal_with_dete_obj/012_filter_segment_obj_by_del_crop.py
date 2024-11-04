# -*- coding: utf-8  -*-
# -*- author: jokker -*-


"""
* 通过将分割对象截图并删除小图的方式，删除分割结果中有问题的对象
    * 面积比较小
    * 不是绝缘子片的范围
    *
"""

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
crop_dir = r"C:\data\004_绝缘子污秽\002_测试标图流程\crop_box_fix\crop_box"
save_dir = r"C:\data\004_绝缘子污秽\002_测试标图流程\json_fix"

index = 1
for each_json_path in FileOperationUtil.re_all_file(json_dir, endswitch=['.json']):

    img_name = FileOperationUtil.bang_path(each_json_path)[1]
    save_json_path = os.path.join(save_dir, img_name + '.json')
    include_labels = []

    a = SegmentRes()
    a.parse_json_info(json_path=each_json_path, parse_mask=False, parse_img=False)

    # 找到未被删除的 crop
    for i in range(len(a)):
        each_label = "test{0}".format(i+1)
        each_crop_path = os.path.join(crop_dir, "{0}_{1}.jpg".format(img_name, each_label))
        if os.path.exists(each_crop_path):
            include_labels.append(each_label)

    a.filter_segment_obj_by_lables(include_labels=include_labels)
    a.save_to_json(save_json_path)

    print(index, each_json_path)
    index += 1



