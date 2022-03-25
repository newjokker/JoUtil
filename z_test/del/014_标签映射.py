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



update_tags = {

    "kkxObj_miss":"K",
    "kkxObj_illegal":"kkxTC",

    # HDObj_clearence、kkxObj_clearence、noObj_clearence、 ULmObj_flat

    "HDObj_clearence":"clearance",
    "kkxObj_clearence":"clearance",
    "noObj_clearence":"clearance",
    "ULmObj_flat":"clearance",

    # kkxObj_noLm 、 noObj_noLm、HDObj_single

    "kkxObj_noLm":"noLm",
    "noObj_noLm":"noLm",
    "HDObj_single":"noLm",

    # HDObj_rust、LmObj_rust、dpObj_rust、kkxObj_rust、noObj_rust

    "HDObj_rust":"xs",
    "LmObj_rust":"xs",
    "dpObj_rust":"xs",
    "kkxObj_rust":"xs",
    "noObj_rust":"xs",

    "dpObj_miss":"dp_missed",

    # PGB_sub_rust、PTTZB_sub_rust、QYB_sub_rust、SJB_sub_rust、TXXJ_sub_rust、UBGB_sub_rust、
    # UBGB_sub_rust、WTGB_sub_rust、XCXJCT_sub_rust、ZGB_sub_rust、BGXJ_sub_rust

    "PGB_sub_rust":"rust",
    "PTTZB_sub_rust":"rust",
    "QYB_sub_rust":"rust",
    "SJB_sub_rust":"rust",
    "TXXJ_sub_rust":"rust",
    "UBGB_sub_rust":"rust",
    "WTGB_sub_rust":"rust",
    "XCXJCT_sub_rust":"rust",
    "ZGB_sub_rust":"rust",
    "BGXJ_sub_rust":"rust",

    "jyhObj_drop":"Miss",

    "jyzObj_bigbang":"jyzzb",

    "Xjfail":"Xjfail",

    # bljyz_rust、tcjyz_rust、

    "bljyz_rust":"jyz_rust",
    "tcjyz_rust":"jyz_rust",

    "fzc_rust":"fzc_rust",

    "nc":"nc",

    "fzc_broken":"fzc_broken",

    "jyhObj_oblique":"fail",


}

xml_dir = r"C:\Users\14271\Desktop\xml_tmp"
save_dir = r"C:\Users\14271\Desktop\xml_tmp"


OperateDeteRes.get_class_count(xml_dir, print_count=True)

for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):
    a = DeteRes(each_xml_path)
    a.filter_by_tags(need_tag=update_tags.keys())
    a.update_tags(update_dict=update_tags)
    save_path = os.path.join(save_dir, os.path.split(each_xml_path)[1])
    a.save_to_xml(save_path)

OperateDeteRes.get_class_count(save_dir, print_count=True)














