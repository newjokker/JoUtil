# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.txkj.imageAugmentation import ImageAugmentation
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.operateDeteRes import OperateDeteRes, OperateTrainData

img_dir = r"C:\Users\14271\Desktop\updata_step_1_train_data\to_fix_extra_data\JPEGImages"
xml_dir = r"C:\Users\14271\Desktop\updata_step_1_train_data\to_fix_extra_data\Annotations"
save_dir = r"C:\Users\14271\Desktop\updata_step_1_train_data\to_fix_extra_data\crop_with_xml"

index = 0
for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):
    index += 1
    print(index, each_xml_path)
    each_img_path = os.path.join(img_dir, FileOperationUtil.bang_path(each_xml_path)[1] + '.jpg')
    a = DeteRes(each_xml_path, assign_img_path=each_img_path)
    a.crop_with_xml(augment_parameter=[0.5,0.5,0.5,0.5], save_dir=save_dir, split_by_tag=True, need_tags=["fzc"])


# OperateDeteRes.get_xml_from_crop_xml(save_dir, img_dir, save_xml_dir=save_new_dir)