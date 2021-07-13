# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.operateDeteRes import OperateDeteRes
xml_dir = r"C:\Users\14271\Desktop\docker_merge\xml"
xml_new_dir = r"C:\Users\14271\Desktop\docker_merge\xml_new"


# for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):
#
#     a = DeteRes()
#     a.xml_path = each_xml_path
#     a.update_tags({"040500013": "K", "040500023": "illegal", "040500033": "K_KG_rust", "040501013": "Lm_rust",})
#     save_path = os.path.join(xml_new_dir, os.path.split(each_xml_path)[1])
#     a.save_to_xml(save_path)



for each in OperateDeteRes.get_class_count(xml_dir).items():
    print(each)
print('-'*100)
for each in OperateDeteRes.get_class_count(xml_new_dir).items():
    print(each)


