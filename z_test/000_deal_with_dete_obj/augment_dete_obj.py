# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.txkjRes.deteRes import DeteRes,DeteObj
from JoTools.utils.FileOperationUtil import FileOperationUtil


xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\999_wait_for_train\武汉电科院_2021_04\xml_new_0.05"


for i in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):
    a = DeteRes(i)
    a.do_augment([0.05,0.05,0.05,0.05], is_relative=True)
    a.save_to_xml(i)

