# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.txkj.imageAugmentation import ImageAugmentation
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.operateDeteRes import OperateDeteRes, OperateTrainData

# img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\JPEGImages"
# xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\Annotations_broken"
# save_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\crop_with_xml"

# index = 0
# for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):
#     index += 1
#     print(index, each_xml_path)
#     each_img_path = os.path.join(img_dir, FileOperationUtil.bang_path(each_xml_path)[1] + '.jpg')
#     a = DeteRes(each_xml_path, assign_img_path=each_img_path)
#     a.crop_with_xml(augment_parameter=[0.5,0.5,0.5,0.5], save_dir=save_dir, split_by_tag=True)




xml_dir = r"C:\Users\14271\Desktop\updata_step_1_train_data\to_fix_extra_data\crop_with_xml"
img_dir= r"C:\Users\14271\Desktop\updata_step_1_train_data\to_fix_extra_data\JPEGImages"
save_dir = r"C:\Users\14271\Desktop\updata_step_1_train_data\to_fix_extra_data\cover_xml"

OperateDeteRes.get_xml_from_crop_xml(xml_dir=xml_dir, region_img_dir=img_dir, save_xml_dir=save_dir)