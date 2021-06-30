# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.for_csdn.word_pic.word_pic import WordImage
from PIL import Image
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil



img_dir = r"C:\Users\14271\Desktop\结果对比\img"
# xml_dir = r"C:\Users\14271\Desktop\结果对比\standard_oly_nc"
xml_dir = r"C:\Users\14271\Desktop\结果对比\merge_update_only_nc"
res_dir = r"C:\Users\14271\Desktop\结果对比\draw"


OperateDeteRes.draw_tags(img_dir=img_dir, xml_dir=xml_dir, save_dir=res_dir)


