# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.utils.FileOperationUtil import FileOperationUtil


img_dir = r"\\192.168.3.80\数据\9eagle数据库\peiyu_06.library\images"
img_dir_2 = r"\\192.168.3.80\数据\9eagle数据库\peiyu_07.library\images"
img_dir_3 = r"\\192.168.3.80\数据\9eagle数据库\peiyu_11.library\images"


id_set = set()
for index, each in enumerate(FileOperationUtil.re_all_folder(img_dir)):
    print(index, each)
    id_set.add(os.path.split(each)[1])

for index, each in enumerate(FileOperationUtil.re_all_folder(img_dir_2)):
    if os.path.split(each)[1] in id_set:
        print("* 重复 ：", each)

for index, each in enumerate(FileOperationUtil.re_all_folder(img_dir_3)):
    if os.path.split(each)[1] in id_set:
        print("* 重复 ：", each)

print("over")
