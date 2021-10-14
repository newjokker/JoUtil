# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.utils.JsonUtil import JsonUtil
import numpy as np
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.operateDeteRes import OperateDeteRes
import os
from JoTools.utils.FileOperationUtil import FileOperationUtil


img_dir = r"C:\Users\14271\Desktop\del\save_fangtian_res"

save_dir = r"C:\Users\14271\Desktop\001_有ground_turth结果"


res = {}

for each_xml_path in FileOperationUtil.re_all_file(img_dir):
    a = DeteRes(each_xml_path)
    a.filter_by_func(lambda x:x.des != "tuxingkeji")
    save_path = os.path.join(save_dir, a.file_name[:-4] + '.xml')
    a.save_to_xml(save_path)

#     each_res = a.count_tags()
#
#     for each in each_res:
#         if each in res:
#             res[each] += each_res[each]
#         else:
#             res[each] = each_res[each]
#
#
# for each in res.items():
#     print(each)
#




