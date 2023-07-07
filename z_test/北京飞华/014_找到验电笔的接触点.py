# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import math
import os.path
import random

from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil


def get_distance(s_x, s_y, x, y):
    return (s_x - x)**2 + (s_y - y)**2

def find_point(s_x, s_y, p_list):
    max_dis = -1
    res_x, res_y = -1, -1
    for each in p_list:
        p_x, p_y = each
        each_dis = get_distance(s_x, s_y, p_x, p_y)
        if each_dis > max_dis:
            res_x = p_x
            res_y = p_y
            max_dis = each_dis
    return res_x, res_y




xml_dir = r"C:\Users\14271\Desktop\北京飞华\022_ts格式的视频截图\xml_test"
save_dir = r"C:\Users\14271\Desktop\北京飞华\022_ts格式的视频截图\res"

index = 0

all_xml_path = list(FileOperationUtil.re_all_file(xml_dir, endswitch=[".xml"]))

random.shuffle(all_xml_path)

for each_xml_path in all_xml_path:

    each_img_path = os.path.join(xml_dir, FileOperationUtil.bang_path(each_xml_path)[1] + ".jpg")
    each_save_path = os.path.join(save_dir, FileOperationUtil.bang_path(each_xml_path)[1] + ".jpg")

    a = DeteRes(each_xml_path)
    a.filter_by_tags(need_tag=["s_yd", "gj_ydb"], update=True)

    # 按照置信度进行排序，只保留一个验电笔和一个验电手
    if a.has_tag("s_yd") and a.has_tag("gj_ydb"):

        yds = a.filter_by_tags(need_tag=["s_yd"], update=False)
        yds = yds.keep_only_by_conf_max()
        s_x, s_y = yds[0].get_center_point()
        s_x += (yds[0].y2 - yds[0].y1) * 0.25

        ydb = a.filter_by_tags(need_tag=["gj_ydb"], update=False)
        ydb = ydb.keep_only_by_conf_max()

        p1, p2, p3, p4 = ydb[0].get_points()

        res_x, res_y = find_point(s_x, s_y, [p1, p2, p3, p4])

        a.add_obj(x1 = res_x-5, y1 = res_y -5, x2= res_x+5, y2=res_y+5, conf=1, tag="point")

        a.img_path = each_img_path

        a.draw_dete_res(each_save_path)

        index += 1
        if index >= 50:
            break














