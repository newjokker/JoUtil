# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.CsvUtil import CsvUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil
import os

def xml_to_csv(xml_dir, csv_save_path):
    """将保存的 xml 文件信息存放在 csv 文件中"""
    csv_list = [['filename', 'code', 'score', 'xmin', 'ymin', 'xmax', 'ymax']]
    #
    for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):
        try:
            dete_res = DeteRes(xml_path=each_xml_path)
            # 输出对应的 csv，filename,code,score,xmin,ymin,xmax,ymax
            for dete_obj in dete_res:
                csv_list.append([each_xml_path[:-3] + 'jpg', dete_obj.tag, dete_obj.conf, dete_obj.x1, dete_obj.y1, dete_obj.x2, dete_obj.y2])
        except Exception as e:
            print('-' * 100)
            print('GOT ERROR---->')
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])
            print(e.__traceback__.tb_lineno)
    CsvUtil.save_list_to_csv(csv_list, csv_save_path)


def merge_xml_list(xml_path_list, save_path):
    """将 xml 进行合并，获取 DeteRes"""
    if len(xml_path_list) == 1:
        a = DeteRes(xml_path=xml_path_list[0])
    elif len(xml_path_list) > 1:
        a = DeteRes(xml_path=xml_path_list[0])
        for each_assign_xml_path in xml_path_list[1:]:
            each_dete_res = DeteRes(xml_path=each_assign_xml_path)
            a += each_dete_res
    else:
        return None
    # fixme 这边要保存为武汉的格式，直接写一个函数
    a.save_to_xml(save_path)


def dete_res_to_xml(dete_res, save_xml_path):
    """将 dete_res 转为 xml 文件"""

    # 按照武汉的格式写一个函数对生成 xml 进行完善
    pass


def merge_xml(xml_dir, save_dir):
    """将 xml_dir 中文件名相同的 xml 进行合并，放到 save_dir 文件夹下"""
    # 合并相同文件名
    xml_dict = {}
    for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):
        each_xml_name = os.path.split(each_xml_path)[1]
        if each_xml_name in xml_dict:
            xml_dict[each_xml_name].append(each_xml_path)
        else:
            xml_dict[each_xml_name] = [each_xml_path]
    # 合并
    for each_xml_name, each_xml_path_list in xml_dict.items():
        save_xml_path = os.path.join(save_dir, each_xml_name)
        merge_xml_list(each_xml_path_list, save_xml_path)


if __name__ == "__main__":

    pass








