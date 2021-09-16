# -*- coding: utf-8  -*-
# -*- author: jokker -*-



from JoTools.utils.JsonUtil import JsonUtil
import numpy as np
from JoTools.txkjRes.deteRes import DeteRes
import os
from JoTools.utils.FileOperationUtil import FileOperationUtil


img_dir = r"C:\Users\14271\Desktop\del\save_fangtian_res"

# todo 统计各个要素的面积大小和偏差


for each_xml_path in FileOperationUtil.re_all_file(img_dir):
    print('-'*50)
    a = DeteRes(each_xml_path)
    have_txkj = False
    have_ok = False
    for each_dete_obj in a:
        if each_dete_obj.des != "tuxingkeji":
            have_txkj = True
        else:
            have_ok = True

    a.print_as_fzc_format()

