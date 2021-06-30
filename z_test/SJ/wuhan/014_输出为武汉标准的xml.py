# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# todo 输出为武汉格式，带 xml

from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.CsvUtil import CsvUtil


def xml_to_csv(xml_dir, csv_save_path):
    """将保存的 xml 文件信息存放在 csv 文件中"""
    csv_list = [['filename', 'code', 'score', 'xmin', 'ymin', 'xmax', 'ymax']]
    #
    for each_xml_path in xml_path_dict:
        try:
            dete_res = DeteRes(xml_path=each_xml_path)
            # 输出对应的 csv，filename,code,score,xmin,ymin,xmax,ymax
            for dete_obj in dete_res:
                each_csv_line = [each_xml_path[:-3] + 'jpg', dete_obj.tag, dete_obj.conf, dete_obj.x1, dete_obj.y1, dete_obj.x2, dete_obj.y2]
                csv_list.append(each_csv_line)
        except Exception as e:
            print('-' * 100)
            print('GOT ERROR---->')
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])
            print(e.__traceback__.tb_lineno)

    CsvUtil.save_list_to_csv(csv_list, csv_save_path)


def merge_xml(xml_dir, save_dir):
    """将 xml_dir 中文件名相同的 xml 进行合并，放到 save_dir 文件夹下"""
    pass













