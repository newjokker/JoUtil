# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.utils.FileOperationUtil import FileOperationUtil

img_dir = r"C:\Users\14271\Desktop\jh\jh_crop\XJfail"


for each_img_path in FileOperationUtil.re_all_file(img_dir):
    # print(each_img_path)

    _,name,_= FileOperationUtil.bang_path(each_img_path)

    name = name.split("-+-")[0]

    print(name)


