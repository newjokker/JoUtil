# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes, DeteObj, DeteAngleObj


img_dir = r"/home/suanfa-3/ldq/002_test_res/fzc_v1.2.5.2_check_error"
save_dir = r"/home/suanfa-3/ldq/002_test_res/fzc_v1.2.5.2_check_error_crop"

index = 0

for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.xml']):
    index += 1
    try:
        a = DeteRes(each_img_path)
        print(index, a.img_path)
        a.crop_and_save(save_dir, split_by_tag=True)
    except Exception as e:
        print(e)



