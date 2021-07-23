# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.txkjRes.segmentJson import SegmentJson
from JoTools.utils.FileOperationUtil import FileOperationUtil
import base64
import numpy as np
from labelme import utils
import labelme
import cv2
from PIL import Image


json_dir = r"C:\data\004_绝缘子污秽\val\json"

a = SegmentJson()

for each_json_path in list(FileOperationUtil.re_all_file(json_dir, endswitch=['.json']))[20:]:

    print(each_json_path)

    a.parse_json_info(each_json_path, parse_img=True, parse_mask=True)

    a.save_mask(r"C:\Users\14271\Desktop\del\del.npy")

    break

a.print_as_fzc_format()


