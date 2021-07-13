# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.for_csdn.word_pic.word_pic import WordImage
from PIL import Image
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil




xml_path = r"C:\Users\14271\Desktop\del\xml\img65.xml"


a = DeteRes(xml_path)

for each_obj in a:
    print(each_obj.crop_path)