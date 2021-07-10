# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
from JoTools.for_csdn.word_pic.word_pic import WordImage
from PIL import Image
import shutil
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.RandomUtil import RandomUtil
from JoTools.utils.TxtUtil import TxtUtil


# crop_dir = r"C:\Users\14271\Desktop\寻找未被发现的fzc_broken\fzc_broken_ok"

# img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\JPEGImages"
# xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\Annotations"
# save_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\001_train_data_step_1.5\fzc_v0.2.5.x_classify\crop_[0,0.2]"

# img_path_list = []
#
# for each_img_path in FileOperationUtil.re_all_file(crop_dir, endswitch=['.jpg']):
#
#     img_name = FileOperationUtil.bang_path(each_img_path)[1]
#     img_name = img_name.split('-+-')[0]
#
#     img_path_list.append([os.path.join("/home/suanfa-3/ldq/002_test_res/fzc_v1.2.5.2_check_error", img_name + '.xml')])
#
# TxtUtil.write_table_to_txt(img_path_list, r"C:\Users\14271\Desktop\寻找未被发现的fzc_broken\img_name.txt", end_line='\n')


# txt_path = r"/home/suanfa-3/ldq/002_test_res/img_name.txt"
txt_path = r"C:\Users\14271\Desktop\寻找未被发现的fzc_broken/img_name.txt"
save_dir = r"/home/suanfa-3/ldq/002_test_res/region_img"
txt_info = TxtUtil.read_as_tableread_as_table(txt_path)

copy_img_list = []

for each in txt_info:

    a = DeteRes(each[0])
    print(a.img_path)

    # copy_img_list.append(a.img_path)

FileOperationUtil.move_file_to_folder(copy_img_list, save_dir, is_clicp=False)

















