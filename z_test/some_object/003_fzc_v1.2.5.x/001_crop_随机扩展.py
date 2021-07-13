# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.for_csdn.word_pic.word_pic import WordImage
from PIL import Image
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.RandomUtil import RandomUtil

img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\JPEGImages"
xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\Annotations"
save_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\001_train_data_step_1.5\fzc_v0.2.5.x_classify\crop_[0.05,0.15]"

for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg']):
    each_xml_path = os.path.join(xml_dir, FileOperationUtil.bang_path(each_img_path)[1] + '.xml')
    #
    if not os.path.exists(each_xml_path):
        continue
    #
    a = DeteRes(each_xml_path)
    a.img_path = each_img_path
    #
    x1 = RandomUtil.rand_range_float(0.05, 0.15)
    x2 = RandomUtil.rand_range_float(0.05, 0.15)
    y1 = RandomUtil.rand_range_float(0.05, 0.15)
    y2 = RandomUtil.rand_range_float(0.05, 0.15)
    #
    print([x1, x2, y1, y2])
    #
    a.crop_and_save(save_dir=save_dir, split_by_tag=True, augment_parameter=[x1, x2, y1, y2])

