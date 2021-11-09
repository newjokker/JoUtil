# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil

xml_dir_001 = r"C:\Users\14271\Desktop\101_save_res"
xml_dir_002 = r"C:\Users\14271\Desktop\221_save_res"

for each_xml_path in FileOperationUtil.re_all_file(xml_dir_001, endswitch=['.xml']):
    each_xml_path_2 = os.path.join(xml_dir_002, os.path.split(each_xml_path)[1])

    a= DeteRes(each_xml_path)
    b = DeteRes(each_xml_path_2)

    if len(a) != len(b):
        a.print_as_fzc_format()
        print('-'*20)
        b.print_as_fzc_format()
        print('-'*50)






