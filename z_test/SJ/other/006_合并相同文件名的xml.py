# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil


def merge_dete_res(xml_path_list, save_dir):
    """将检测结果进行合并"""

    xml_name = os.path.split(xml_path_list[0])[1]
    xml_name = xml_name[:len(str(xml_name).split("-+-")[0])]
    # save_path = os.path.join(save_dir, xml_name + '.xml')
    save_path = os.path.join(save_dir, xml_name)

    # 获取第一个要素
    dete_res = DeteRes(xml_path=xml_path_list[0])
    # off_x, off_y = get_offset_from_name(xml_path_list[0])
    # dete_res.offset(off_x, off_y)

    if len(xml_path_list) == 1:
        dete_res.save_to_xml(save_path)
    else:
        for each in xml_path_list[1:]:
            each_dete_res = DeteRes(xml_path=each)
            # off_x, off_y = get_offset_from_name(each)
            # each_dete_res.offset(off_x, off_y)
            dete_res += each_dete_res
        dete_res.save_to_xml(save_path)


if __name__ == "__main__":

    xml_dir = r"C:\Users\14271\Desktop\10kV_total_data\xml_old"
    save_dir = r"C:\Users\14271\Desktop\xml_test"

    xml_dict = {}

    for each_xml in FileOperationUtil.re_all_file(xml_dir, lambda x:str(x).endswith('.xml')):
        xml_name = os.path.split(each_xml)[1]
        # xml_name = xml_name[:len(str(xml_name).split("-+-")[0])]

        if xml_name in xml_dict:
           xml_dict[xml_name].append(each_xml)
        else:
            xml_dict[xml_name] = [each_xml]


    for each_xml in xml_dict:
        if len(xml_dict[each_xml]) > 0:
            merge_dete_res(xml_dict[each_xml], save_dir)







