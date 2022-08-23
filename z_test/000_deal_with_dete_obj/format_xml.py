# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import sys
import argparse
from JoTools.txkjRes.deteRes import DeteRes,DeteObj
from JoTools.utils.FileOperationUtil import FileOperationUtil

xml_dir = r"D:\data\001_fzc_优化相关资料\dataset_fzc\000_0_标准测试集\Annotations"

index = 0
for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):

    a = DeteRes(each_xml_path)
    a.angle_obj_to_obj()
    a.save_to_xml(each_xml_path)

    index += 1
    print(index, each_xml_path)






