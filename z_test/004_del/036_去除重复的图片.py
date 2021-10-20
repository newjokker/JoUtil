# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from  JoTools.utils.FileOperationUtil import FileOperationUtil



normal_dir = r"F:\20211019_防震锤锈蚀数据清洗\fzc_rust_fix_1\fzc_rust_2"
rust_dir = r"F:\20211019_防震锤锈蚀数据清洗\fzc_rust_fix_1\fzc_rust2rust"
other_dir = r"F:\20211019_防震锤锈蚀数据清洗\fzc_already\fzc_normal2other"


for each_img_path in FileOperationUtil.re_all_file(rust_dir, endswitch=['.jpg']):
    normal_path = os.path.join(normal_dir, os.path.split(each_img_path)[1])

    if os.path.exists(normal_path):
        os.remove(normal_path)
        print(normal_path)
    else:
        print("meiyou")











