# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os

import numpy as np
import shutil
from JoTools.txkjRes.segmentRes import SegmentRes, SegmentOpt
from JoTools.utils.FileOperationUtil import FileOperationUtil


mask_dir = r"C:\Users\14271\Desktop\temp"
json_dir = r"C:\Users\14271\Desktop\用于测试的分割数据\img_json"
save_dir = r"C:\Users\14271\Desktop\用于测试的分割数据\train_json"


for each_json_path in FileOperationUtil.re_all_file(mask_dir):

    each_json_path = os.path.join(json_dir, FileOperationUtil.bang_path(each_json_path)[1] + ".json")

    a = SegmentRes(json_path=each_json_path)
    a.parse_json_info(parse_mask=True)

    # a.(os.path.join(save_dir, FileOperationUtil.bang_path(each_json_path)[1] + ".jpg"))

    np.save(os.path.join(save_dir, FileOperationUtil.bang_path(each_json_path)[1] + ".npy"), a.mask)

    shutil.copy(each_json_path[:-4] + "jpg", os.path.join(save_dir, FileOperationUtil.bang_path(each_json_path)[1] + ".jpg"))












