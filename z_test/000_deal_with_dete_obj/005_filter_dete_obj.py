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



xml_dir = r"/home/ldq/ucd_dir/wuhan/merge_xml"
save_dir = r"/home/ldq/ucd_dir/wuhan/merge_except_filter"

cut_tags = [

"040500031",
"040500032",
"040500033",
"040501023",
"040501022",
"040501021",
"040501031",
"040501032",
"040501033",

"010103011",
"010103012",
"010103013",
"010002011",
"010002012",
"010002013",
"010404011",
"010404012",
"010404013",

"020000011",
"020000012",
"020000013",
"020000021",
"020000022",
"020000023",
"020000031",
"020000032",
"020000033",
"030000041",
"030000042",
"030000043",

"030000081",
"030000082",
"030000083",
"030200061",
"030200062",
"030200063",
"030200111",
"030200112",
"030200113",
"030200121",
"030200122",
"030200123",
"030200141",
"030200142",
"030200143",
"040001021",
"040001022",
"040001023",
    ]


OperateDeteRes.get_class_count(xml_dir, print_count=True)

for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):
    #
    a = DeteRes(each_xml_path)
    a.filter_by_tags(remove_tag=cut_tags)
    save_path = os.path.join(save_dir, os.path.split(each_xml_path)[1])

    a.save_to_xml(save_path)

OperateDeteRes.get_class_count(save_dir, print_count=True)




