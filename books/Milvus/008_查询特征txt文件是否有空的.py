# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.utils.FileOperationUtil import FileOperationUtil


txt_dir = r"C:\Users\14271\Desktop\feature_txt_old"


for each_txt_path in FileOperationUtil.re_all_file(txt_dir, endswitch=[".txt"]):

    file_size = os.path.getsize(each_txt_path)

    if file_size != 12800:

        print(file_size, each_txt_path)


