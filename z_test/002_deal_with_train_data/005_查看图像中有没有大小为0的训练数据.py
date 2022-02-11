# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.utils.FileOperationUtil import FileOperationUtil, FilterFun

img_dir = r"C:\Users\14271\Desktop\del"


for each_img_path in FileOperationUtil.re_all_file(img_dir, func=FilterFun.get_filter_about_file_size(1, mode='bt')):
    img_size = os.path.getsize(each_img_path)
    print(img_size)
    # if img_size == 0:
    #     os.remove(each_img_path)
    #     print(each_img_path)








