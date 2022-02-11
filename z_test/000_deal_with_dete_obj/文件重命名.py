# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
import shutil
from JoTools.utils.FileOperationUtil import FileOperationUtil

img_dir = r"D:\data\001_fzc_优化相关资料\dataset_fzc\001_train_data_step_1.5\jieya\zd\extend"

for each_img_path in FileOperationUtil.re_all_file(img_dir):

    print(each_img_path)

    img_dir, img_name, suffix = FileOperationUtil.bang_path(each_img_path)

    new_img_path = os.path.join(img_dir, img_name + '_extend.' + suffix)

    shutil.move(each_img_path, new_img_path)



