# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
import shutil
from JoTools.operateDeteRes import OperateDeteRes



xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\Annotations_big_small\xml"
img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\JPEGImages"
save_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\Annotations_big_small\crop"


OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True)

