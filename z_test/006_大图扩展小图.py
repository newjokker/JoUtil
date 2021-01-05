# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.txkj.databaseKG import DatabaseKG
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.detectionResult import OperateDeteRes, DeteRes, DeteObj
from JoTools.txkj.parseXml import parse_xml


# --------------------------------------------------------------------------------------------------------
xmlDir = r"C:\Users\14271\Desktop\add_other_info\Annotations"
imgDir = r"C:\Users\14271\Desktop\add_other_info\JPEGImages"
saveDir = r"C:\Users\14271\Desktop\123"


small_img_count_dict = {

    2:1,
    3:1,
    4:2,
    5:3,
    6:4,
    7:8,
    8:10,
}


for index, each_xml_path in enumerate(FileOperationUtil.re_all_file(xmlDir, lambda x: str(x).endswith((".xml")))):
    print(index, each_xml_path)

    each_img_path = os.path.join(imgDir, os.path.split(each_xml_path)[1][:-4] + '.jpg')

    xml_info = parse_xml(each_xml_path)

    if len(xml_info['object']) in small_img_count_dict:
        each_small_img_count = small_img_count_dict[len(xml_info['object'])]
    else:
        each_small_img_count = 10

    DatabaseKG.get_subset_from_pic(each_xml_path, each_img_path, saveDir, min_count=2, small_img_count=each_small_img_count)
# --------------------------------------------------------------------------------------------------------
