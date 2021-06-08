# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import shutil
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes

img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\002_train_data_step_2\20210507\fzc_yt"
xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\002_train_data_step_2\20210507\fzc_yt"
as_broken_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\002_train_data_step_2\20210507\fzc_yt_new\as_broken"
have_extra_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\002_train_data_step_2\20210507\fzc_yt_new\have_extra"
normal_extra_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\002_train_data_step_2\20210507\fzc_yt_new\normal"

for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):
    each_img_path = each_xml_path[:-3] + 'jpg'
    a = DeteRes(each_xml_path)

    tag_count = a.count_tags()


    if 'single' not in tag_count or 'middle_pole' not in tag_count or tag_count['single'] < 2  or tag_count['middle_pole'] < 1:
        print("broken")
        new_xml_path = os.path.join(as_broken_dir, os.path.split(each_xml_path)[1])
        new_img_path = os.path.join(as_broken_dir, os.path.split(each_img_path)[1])
        shutil.move(each_img_path, new_img_path)
        shutil.move(each_xml_path, new_xml_path)
    elif tag_count['single'] > 2 or tag_count['middle_pole'] > 1:
        print("extra")
        new_xml_path = os.path.join(have_extra_dir, os.path.split(each_xml_path)[1])
        new_img_path = os.path.join(have_extra_dir, os.path.split(each_img_path)[1])
        shutil.move(each_img_path, new_img_path)
        shutil.move(each_xml_path, new_xml_path)
    else:
        new_xml_path = os.path.join(normal_extra_dir, os.path.split(each_xml_path)[1])
        new_img_path = os.path.join(normal_extra_dir, os.path.split(each_img_path)[1])
        shutil.move(each_img_path, new_img_path)
        shutil.move(each_xml_path, new_xml_path)

    print(tag_count)





