# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil


xml_dir = r"C:\Users\14271\Desktop\北京飞华\025_优化签字\xml"
xml_res_dir = r"C:\Users\14271\Desktop\北京飞华\025_优化签字\xml_res"

xml_path_list = []

index = 0
for each_xml in FileOperationUtil.re_all_file(xml_dir, endswitch=[".xml"]):
    index += 1
    a = DeteRes(each_xml)

    a.filter_by_tags(need_tag=["kg_big", "kg_small"], update=True)

    if len(a) == 2:
        if a[0].tag == a[1].tag:
            print(index, each_xml)
            xml_path_list.append(each_xml)

FileOperationUtil.move_file_to_folder(xml_path_list, xml_res_dir)




