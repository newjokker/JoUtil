# -*- coding: utf-8  -*-
# -*- author: jokker -*-



# todo 只保留一定置信度的 标签，删除其他的标签

import os
import shutil
from JoTools.utils.JsonUtil import JsonUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.operateDeteRes import OperateDeteRes


#  每个标签不放回地从 extra 找 1000/5 张图片，要求图片中对应的对象数目最多
# ----------------------------------------------------------------------------------------------------------------------
xml_dete_dir = r"C:\Users\14271\Desktop\xml_recommend\Annonations_extra"                # 预测出来的 xml 文件夹
save_xml_dir = r"C:\Users\14271\Desktop\xml_recommend\Annonations_extra"
conf_range = [0.35, 0.75]
# -----------------------------------------------------------------------------------------------------------------------


for each_xml_path in FileOperationUtil.re_all_file(xml_dete_dir, endswitch=[".xml"]):
    dete_res = DeteRes(each_xml_path)
    dete_res.filter_by_conf(conf_range[0], mode='gt')
    dete_res.filter_by_conf((conf_range[1]), mode='lt')
    each_uc = FileOperationUtil.bang_path(each_xml_path)[1]
    save_xml_path = os.path.join(save_xml_dir, each_uc + ".xml")
    dete_res.save_to_xml(save_xml_path)









