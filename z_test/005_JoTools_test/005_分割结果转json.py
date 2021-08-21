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

"""
* mask 的理想状态是每一个对象用一个不同的 int 值表示出来
* mask 的次理想状态是每一个对象用相同的 int 值表示出来
"""


img_dir = r"C:\Users\14271\Desktop\mask_test_res_019\img"
mask_dir = r"C:\Users\14271\Desktop\mask_test_res_019\mask"
save_dir = r"C:\Users\14271\Desktop\mask_test_res_019\json"


for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg']):
    each_mask_path = os.path.join(mask_dir, FileOperationUtil.bang_path(each_img_path)[1] + '_mask.png')
    each_save_path = os.path.join(save_dir, FileOperationUtil.bang_path(each_img_path)[1] + '.json')

    if not os.path.exists(each_mask_path):
        print("* mask 文件不存在")
        continue
    else:
        print(each_mask_path)

    a = SegmentRes()
    a.img_path = each_img_path
    a.get_segment_obj_from_mask(each_mask_path, each_mask_point_numb=60)
    a.save_to_josn(each_save_path)



