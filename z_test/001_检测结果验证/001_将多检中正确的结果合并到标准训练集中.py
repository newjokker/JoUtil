# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.for_csdn.word_pic.word_pic import WordImage
from PIL import Image
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil



xml_stand_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_0_标准测试集\xml"
xml_extra_dir = r"C:\Users\14271\Desktop\fzc_v1.2.5.0\test_img_016_extra_xml"


for each in OperateDeteRes.get_class_count(xml_stand_dir).items():
    print(each)
print("-"*100)


for each_xml_path in FileOperationUtil.re_all_file(xml_extra_dir, endswitch=['.xml']):
    each_stand_xml = os.path.join(xml_stand_dir, os.path.split(each_xml_path)[1])
    if os.path.exists(each_stand_xml):
        a = DeteRes(each_xml_path)
        b = DeteRes(each_stand_xml)
        c = a + b
        c.save_to_xml(each_stand_xml)

for each in OperateDeteRes.get_class_count(xml_stand_dir).items():
    print(each)
