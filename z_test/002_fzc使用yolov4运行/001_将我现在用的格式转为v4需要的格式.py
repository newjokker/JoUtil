# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.txkjRes.deteXml import ParseXml
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.operateDeteRes import OperateDeteRes

xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\Annotations_one"
save_xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\Annotations_one"


# for each in OperateDeteRes.get_class_count(xml_dir).items():
#     print(each)
#
#
#
# up_tags = {
#     "fzc_yt":"fzc",
#     "fzc_sm":"fzc",
#     "fzc_gt":"fzc",
#     "zd_yt":"fzc",
#     "zd_sm":"fzc",
#     "zd_gt":"fzc",
#     "qx_yt":"fzc",
#     "qx_sm":"fzc",
#     "qx_gt":"fzc",
#     "fzc_broken":"fzc",
# }
#
#
#     # 将各种类型进行合并
#     a = DeteRes(each_xml_path)
#     a.update_tags(up_tags)
#     a.filter_by_tags(remove_tag=["other"])
#     a.save_to_xml(each_xml_path)
#
# print('-'*100)

for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):

    # # 增加字段
    a = ParseXml()
    xml_info = a.get_xml_info(each_xml_path)
    #
    for each in xml_info["object"]:
        each["pose"] = 'Unspecified'
        each["truncated"] = '0'
        each["difficult"] = '0'
    #
    save_path = os.path.join(save_xml_dir, os.path.split(each_xml_path)[1])
    a.save_to_xml(each_xml_path)

