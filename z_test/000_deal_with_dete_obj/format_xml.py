# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import sys
import argparse
from JoTools.txkjRes.deteRes import DeteRes,DeteObj
from JoTools.utils.FileOperationUtil import FileOperationUtil



xml_dir = r"C:\data\003_塔下站人\train\Annotations"


for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):

    a = DeteRes(each_xml_path)
    a.angle_obj_to_obj()
    a.save_to_xml(each_xml_path)
