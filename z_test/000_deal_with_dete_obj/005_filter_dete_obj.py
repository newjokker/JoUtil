# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import random
import os
import shutil
import cv2
import PIL.Image as Image
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes,DeteObj
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.RandomUtil import RandomUtil



xml_dir = r"E:\多标签分类\jyz_test\rename_data\Annotations_only_flaw"
save_dir = r"E:\多标签分类\jyz_test\rename_data\Annotations_only_ps"



OperateDeteRes.get_class_count(xml_dir, print_count=True)

for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):
    #
    a = DeteRes(each_xml_path)
    a.filter_by_tags(need_tag=['tcjyz_single_ps', 'fhjyz_broken'])
    save_path = os.path.join(save_dir, os.path.split(each_xml_path)[1])

    if len(a) > 0:
        a.save_to_xml(save_path)

OperateDeteRes.get_class_count(save_dir, print_count=True)




