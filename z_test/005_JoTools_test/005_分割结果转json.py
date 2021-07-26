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

img_dir = r"C:\Users\14271\Desktop\mask_test_res"
mask_dir = r"C:\Users\14271\Desktop\mask_test_res"
save_dir = r"C:\Users\14271\Desktop\mask_test_res\json"




for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg']):
    each_mask_path = os.path.join(mask_dir, FileOperationUtil.bang_path(each_img_path)[1] + '_mask.png')
    each_save_path = os.path.join(save_dir, FileOperationUtil.bang_path(each_img_path)[1] + '.json')

    a = SegmentRes()
    a.img_path = each_img_path
    a.get_segment_obj_from_mask(each_mask_path, each_mask_point_numb=30)
    a.save_to_josn(each_save_path)

