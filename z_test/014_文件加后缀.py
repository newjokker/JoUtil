# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.utils.FileOperationUtil import FileOperationUtil
import os
import shutil

img_dir = r"C:\Users\14271\Desktop\compare\新旧版本K多检和漏检对比\old_miss_K"

copy_list = []
for each_img_path in FileOperationUtil.re_all_file(img_dir):
    new_img_path = os.path.join(os.path.split(each_img_path)[0], os.path.split(each_img_path)[1][:-4] + '_old.jpg')
    os.rename(each_img_path, new_img_path)




