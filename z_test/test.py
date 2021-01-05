# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.operateResXml import OperateResXml
from JoTools.txkjRes.detectionResult import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil

xml_path = r"C:\Users\14271\Desktop\del\test.xml"
img_path = r"C:\Users\14271\Desktop\del\test.jpg"

xml_dir = r"C:\Users\14271\Desktop\test"

xml_list = FileOperationUtil.re_all_file(xml_dir, lambda x: str(x).endswith('.xml'))

OperateResXml.show_class_count(xml_dir)



# 更新标签
for xml_index, each_xml_path in enumerate(xml_list):
    #
    each_dete_res = DeteRes(each_xml_path)
    each_dete_res.do_nms_in_assign_tags(['KG', 'K', 'Lm'], 0.1)
    each_dete_res.save_to_xml(each_xml_path)

OperateResXml.show_class_count(xml_dir)

