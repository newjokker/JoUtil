# -*- coding: utf-8  -*-
# -*- author: jokker -*-



# todo 只保留一定置信度的 标签，删除其他的标签， 然后做 tag_num_first 操作

import os
import shutil
from JoTools.utils.JsonUtil import JsonUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.operateDeteRes import OperateDeteRes


# #  每个标签不放回地从 extra 找 1000/5 张图片，要求图片中对应的对象数目最多
# # ----------------------------------------------------------------------------------------------------------------------
# xml_dete_dir = r"C:\Users\14271\Desktop\xml_recommend\base_dete_extra_[0.35,0.75]"                # 预测出来的 xml 文件夹
# save_xml_dir = r"C:\Users\14271\Desktop\xml_recommend\base_dete_extra_[0.35,0.75]"
# conf_range = [0.35, 0.75]
# # -----------------------------------------------------------------------------------------------------------------------
#
#
#
# for each_xml_path in FileOperationUtil.re_all_file(xml_dete_dir, endswitch=[".xml"]):
#     dete_res = DeteRes(each_xml_path)
#     dete_res.filter_by_conf(conf_range[0], mode='gt')
#     dete_res.filter_by_conf((conf_range[1]), mode='lt')
#     each_uc = FileOperationUtil.bang_path(each_xml_path)[1]
#     save_xml_path = os.path.join(save_xml_dir, each_uc + ".xml")
#     dete_res.save_to_xml(save_xml_path)
#

# ----------------------------------------------------------------------------------------------------------------------
xml_dete_dir = r"C:\Users\14271\Desktop\xml_recommend\base_dete_extra_[0.35,0.75]"                # 预测出来的 xml 文件夹
xml_stand_dir = r"C:\Users\14271\Desktop\xml_recommend\Annonations_extra"               # 标准的 xml 文件夹
save_dir = r"C:\Users\14271\Desktop\xml_recommend\Annonations_tag_gradient_first"            # 保存需要的标准 xml 的文件夹
tag_list = ["fzc", "nc", "xj", "jyz", "ring"]                                           # 需要进行寻找和排序的标签
need_xml_count = 1000                                                                   # 需要的 xml 的个数
# -----------------------------------------------------------------------------------------------------------------------

every_tag_xml_count = int(need_xml_count / len(tag_list))
label_count_list = []

# 获取标签分布字典
for each_xml_path in FileOperationUtil.re_all_file(xml_dete_dir, endswitch=[".xml"]):
    each_dete_res = DeteRes(each_xml_path)
    each_uc = FileOperationUtil.bang_path(each_xml_path)[1]
    tag_count_dict = each_dete_res.count_tags()
    tag_count_dict["uc"] = each_uc

    for each_tag in tag_list:
        if each_tag not in tag_count_dict:
            tag_count_dict[each_tag] = 0
    label_count_list.append(tag_count_dict)

# 对字典进行排序，找需要的标签
for each_tag in tag_list:
    label_count_list.sort(key=lambda x:x[each_tag], reverse=True)
    for i in range(every_tag_xml_count):
        each_uc = label_count_list[i]["uc"]
        each_xml_path = os.path.join(xml_stand_dir, each_uc + ".xml")
        save_xml_path = os.path.join(save_dir, each_uc + ".xml")
        shutil.copy(each_xml_path, save_xml_path)
    label_count_list = label_count_list[every_tag_xml_count:]

OperateDeteRes.get_class_count(save_dir, print_count=True)






