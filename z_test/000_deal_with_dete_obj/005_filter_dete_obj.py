# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import random
import os
import shutil
import cv2
import PIL.Image as Image
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes,DeteObj
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.RandomUtil import RandomUtil



xml_dir = r"C:\Users\14271\Desktop\xml_tmp"
save_dir = r"C:\Users\14271\Desktop\xml_tmp"



need_tag_list = ["kkxObj_miss",
                 "DBTZB_sub_rust","PGB_sub_rust", "PTTZB_sub_rust", "QYB_sub_rust", "SJB_sub_rust", "TXXJ_sub_rust",
                 "UBGB_sub_rust", "UGH_sub_rust","WTGB_sub_rust","XCXJCT_sub_rust","ZGB_sub_rust","BGXJ_sub_rust",
                 "jyhObj_drop", "jyzObj_bigbang", "XJfail", "HDObj_clearence", "kkxObj_clearence", "noObj_clearence",
                 "jyz_gm_rust", "fzc_rust", "dpObj_miss", "kkxObj_illegal", "nc", "HDObj_rust", "LmObj_rust", "dpObj_rust",
                 "kkxObj_rust", "noObj_rust",  "fzc_broken", "jyhObj_oblique"
                 ]


OperateDeteRes.get_class_count(xml_dir, print_count=True)

for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):
    #
    a = DeteRes(each_xml_path)
    a.filter_by_tags(need_tag=need_tag_list)
    save_path = os.path.join(save_dir, os.path.split(each_xml_path)[1])

    # if len(a) > 0:
    a.save_to_xml(save_path)

OperateDeteRes.get_class_count(save_dir, print_count=True)
