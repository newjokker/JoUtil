# -*- coding: utf-8  -*-
# -*- author: jokker -*-


# todo 数据均衡优先


import os
import shutil
from JoTools.utils.JsonUtil import JsonUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.operateDeteRes import OperateDeteRes


# todo 根据各个标签个数的比例来分配所有的数据，fzc_num / all_num

# ----------------------------------------------------------------------------------------------------------------------
xml_dete_dir = r"C:\Users\14271\Desktop\xml_recommend\Annonations_extra"                # 预测出来的 xml 文件夹
save_xml_dir = r"C:\Users\14271\Desktop\xml_recommend\Annonations_extra"
region_tag_count_dict = {"fzc": 3432, "jyz": 3772, "nc": 595, "ring":1234, "xj":2460}
extra_uc_tag = "nc"
need_xml_count = 1000
# -----------------------------------------------------------------------------------------------------------------------

count_all = sum(region_tag_count_dict.values())

use_uc_count_dict = {}
weight_dict = {}
weight_list = []
for each_tag in region_tag_count_dict:
    each_count = region_tag_count_dict[each_tag]
    each_weright = (count_all - each_count) / count_all
    weight_list.append(each_weright)
weight_all = sum(weight_list)

for each_tag in region_tag_count_dict:
    each_count = region_tag_count_dict[each_tag]
    each_weright = (count_all - each_count) / count_all
    weight_dict[each_tag] = each_weright / weight_all
    use_uc_count_dict[each_tag] = int((each_weright / weight_all) * need_xml_count)

# 将剩余的数据给指定的模型的标签
use_uc_count_dict[extra_uc_tag] += need_xml_count - sum(use_uc_count_dict.values())













