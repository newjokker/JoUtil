# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
import shutil
from JoTools.utils.FileOperationUtil import FileOperationUtil

region_dir = r"/home/suanfa-5/ldq/002_test_data/69G塔基检出"
result_dir = r"/home/ldq/tj_dete/train_data/JPEGImages"
save_dir = r"/home/suanfa-5/ldq/002_test_data/69G塔基未检出"

for each_img_path in FileOperationUtil.re_all_file(region_dir, endswitch=['.jpg', '.JPG', '.png', '.PNG']):

    print(each_img_path)

    img_name = os.path.split(each_img_path)[1]

    result_path = os.path.join(result_dir, img_name)

    if os.path.exists(result_path):
        shutil.move(each_img_path, os.path.join(save_dir, img_name))









