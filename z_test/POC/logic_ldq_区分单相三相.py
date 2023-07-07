# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil


xml_dir = r"C:\Users\14271\Desktop\POC\gt"
dx_dir = r"C:\Users\14271\Desktop\POC\gt_dx"
sx_dir = r"C:\Users\14271\Desktop\POC\gt_sx"

dx_path_list = []
sx_path_list = []

for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=[".xml"]):

    a = DeteRes(each_xml_path)
    a.filter_by_tags(need_tag=["red","blue","yellow","black","green"])

    tags_count = a.count_tags()

    if "blue" in tags_count and "red" in tags_count:
        if tags_count["blue"] == 2 and tags_count["red"] == 2:
            dx_path_list.append(each_xml_path)
        else:
            sx_path_list.append(each_xml_path)
    else:
        sx_path_list.append(each_xml_path)


FileOperationUtil.move_file_to_folder(dx_path_list, dx_dir, is_clicp=False)
FileOperationUtil.move_file_to_folder(sx_path_list, sx_dir, is_clicp=False)





