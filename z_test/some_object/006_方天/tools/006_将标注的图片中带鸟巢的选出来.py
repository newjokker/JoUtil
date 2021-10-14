# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.utils.JsonUtil import JsonUtil
import numpy as np
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.operateDeteRes import OperateDeteRes
import os
from JoTools.utils.FileOperationUtil import FileOperationUtil


xml_dir = r"C:\Users\14271\Desktop\001_有ground_turth结果"

save_dir = r"C:\Users\14271\Desktop\002_标注的结果中带鸟巢的"


for each_xml_path in FileOperationUtil.re_all_file(xml_dir):
    a = DeteRes(each_xml_path)
    a.filter_by_tags(['010000021'])

    if len(a) > 0:
        a.save_to_xml(os.path.join(save_dir, FileOperationUtil.bang_path(each_xml_path)[1] + '.xml'))







