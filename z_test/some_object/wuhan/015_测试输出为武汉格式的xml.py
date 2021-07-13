# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.for_csdn.word_pic.word_pic import WordImage
from PIL import Image
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil


xml_dir = r"C:\Users\14271\Desktop\del\Annotations"
save_dir = r"C:\Users\14271\Desktop\del\Annotations_wuhan"



for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):

    a = DeteRes(each_xml_path)

    a.save_to_xml(os.path.join(save_dir, os.path.split(each_xml_path)[1]), format='wuhan')

    # print(each_xml_path)

