# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.for_csdn.word_pic.word_pic import WordImage
from PIL import Image
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil



xml_stand_dir = r"C:\Users\14271\Desktop\updata_step_1_train_data\crop_fix_by_ldq\Annotations_broken"
xml_extra_dir = r"C:\Users\14271\Desktop\updata_step_1_train_data\crop_fix_by_ldq\extra_xml"


OperateDeteRes.get_class_count(xml_stand_dir, print_count=True)

for each_xml_path in FileOperationUtil.re_all_file(xml_extra_dir, endswitch=['.xml']):
    each_stand_xml = os.path.join(xml_stand_dir, os.path.split(each_xml_path)[1])
    if os.path.exists(each_stand_xml):
        a = DeteRes(each_xml_path)
        b = DeteRes(each_stand_xml)
        c = a + b
        c.save_to_xml(each_stand_xml)

OperateDeteRes.get_class_count(xml_stand_dir, print_count=True)
