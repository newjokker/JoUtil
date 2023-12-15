# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from PIL import Image
from JoTools.txkjRes.operateDeteRes import OperateDeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil



img_dir = r"C:\Users\14271\Desktop\draw"
# xml_dir = r"C:\Users\14271\Desktop\结果对比\standard_oly_nc"
xml_dir = r"C:\Users\14271\Desktop\draw"
res_dir = r"C:\Users\14271\Desktop\draw_res"


OperateDeteRes.draw_tags(img_dir=img_dir, xml_dir=xml_dir, save_dir=res_dir)


