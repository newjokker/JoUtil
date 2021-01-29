# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil

xml_dir = r"C:\Users\14271\Desktop\10kV_total_data\xml_old\xml_small"



for each_xml_path in FileOperationUtil.re_all_file(xml_dir, lambda x:str(x).endswith('.xml')):

    a = DeteRes(xml_path=each_xml_path)
    a.do_nms(0.3, ignore_tag=True)
    a.save_to_xml(each_xml_path)

