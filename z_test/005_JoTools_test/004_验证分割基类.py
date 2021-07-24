# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.txkjRes.segmentJson import SegmentJson
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil
import base64
import numpy as np
from labelme import utils
import labelme
import cv2
from PIL import Image


json_dir = r"C:\data\004_绝缘子污秽\val\json"

a = SegmentJson()
dete_res = DeteRes()

for each_json_path in list(FileOperationUtil.re_all_file(json_dir, endswitch=['.json']))[20:]:

    print(each_json_path)

    a.parse_json_info(each_json_path, parse_img=True, parse_mask=True)

    dete_res.img = Image.fromarray(a.image_data)

    for each_obj in a.shapes:
        print(each_obj.box)
        box = each_obj.box
        dete_res.add_obj(box[0], box[1], box[2], box[3], tag=each_obj.label)

    b = Image.fromarray(a.mask.astype(np.uint8)*100)
    b.save(r"C:\Users\14271\Desktop\del\112233.jpg")

    dete_res.draw_dete_res(r"C:\Users\14271\Desktop\del\1100.jpg")

    # a.save_mask(r"C:\Users\14271\Desktop\del\del.npy")

    break

a.print_as_fzc_format()






