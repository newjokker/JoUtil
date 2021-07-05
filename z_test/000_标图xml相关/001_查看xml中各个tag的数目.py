# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.for_csdn.word_pic.word_pic import WordImage
from PIL import Image
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil


# xml_dir = r"C:\Users\14271\Desktop\002_test_res_0.6"
xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\fix_obj_range\xml"

OperateDeteRes.get_class_count(xml_dir, print_count=True)

# for each in OperateDeteRes.get_class_count(xml_dir).items():
#     print(each)
#
# print('-'*100)
#
# xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\Annotations_broken"
#
# for each in OperateDeteRes.get_class_count(xml_dir).items():
#     print(each)
#
