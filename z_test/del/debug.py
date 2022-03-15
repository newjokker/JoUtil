# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.operateDeteRes import OperateDeteRes

from collections import Counter

# xml_dir_there = r"C:\Users\14271\Desktop\xml_compare\xml_there"
# xml_dir_here = r"C:\Users\14271\Desktop\xml_compare\xml_here"
#
# xml_here_ok = r"C:\Users\14271\Desktop\xml_compare\xml_here_ok"
# xml_there_ok = r"C:\Users\14271\Desktop\xml_compare\xml_there_ok"
#
# xml_ok_list_here = []
# xml_ok_list_there = []
#
# for each_xml_path in FileOperationUtil.re_all_file(xml_dir_here, endswitch=['.xml']):
#     xml_dir, xml_name = os.path.split(each_xml_path)
#     xml_path_there = os.path.join(xml_dir_there, xml_name)
#     if os.path.exists(xml_path_there):
#         xml_ok_list_here.append(each_xml_path)
#         xml_ok_list_there.append(xml_path_there)
#     else:
#         print("not ok")
#
#
# FileOperationUtil.move_file_to_folder(xml_ok_list_here, xml_here_ok)
# FileOperationUtil.move_file_to_folder(xml_ok_list_there, xml_there_ok)

# a = OperateDeteRes.get_class_count(r"C:\Users\14271\Desktop\xml_compare\xml_here_ok", print_count=True)
# b = OperateDeteRes.get_class_count(r"C:\Users\14271\Desktop\xml_compare\xml_there_ok", print_count=True)


xml_ok_there = r"C:\Users\14271\Desktop\xml_compare\xml_there_ok"
xml_ok_here = r"C:\Users\14271\Desktop\xml_compare\xml_here_ok"

res = []

for each_xml_path in FileOperationUtil.re_all_file(xml_ok_there, endswitch=['.xml']):
    xml_dir, xml_name = os.path.split(each_xml_path)
    xml_path_here = os.path.join(xml_ok_here, xml_name)

    a = DeteRes(each_xml_path)
    b = DeteRes(xml_path_here)

    a = a.filter_by_tags(['xd_missed'], update=True)
    b = b.filter_by_tags(['xd_missed'], update=True)

    c = a + b
    c.do_nms(0.1)

    if len(c) != 0:
        res.append((len(a) + len(b)) / max(len(c), 1))


ct = Counter(res)

print(ct)