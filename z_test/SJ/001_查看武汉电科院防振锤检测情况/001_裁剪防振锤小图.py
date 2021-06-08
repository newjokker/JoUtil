# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.operateDeteRes import OperateDeteRes

img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\JPEGImages"
xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\Annotations_broken"
save_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\crop"


for each in OperateDeteRes.get_class_count(xml_dir).items():
    print(each)
    print('-'*30)

# OperateDeteRes.crop_imgs(img_dir=img_dir, xml_dir=xml_dir, save_dir=save_dir, split_by_tag=True, augment_parameter=[0.3,0.3,0.3,0.3])

