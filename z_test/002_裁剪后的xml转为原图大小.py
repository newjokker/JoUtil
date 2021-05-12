# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.deteRes import DeteRes
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil

xml_dir = r"C:\data\fzc_优化相关资料\001_新标注fzc图\crop_extend_0.2"
img_dir = r"C:\data\fzc_优化相关资料\000_等待训练\JPEGImages"
save_dir = r"C:\data\fzc_优化相关资料\001_新标注fzc图\xml"


OperateDeteRes.get_xml_from_crop_xml(xml_dir=xml_dir, region_img_dir=img_dir, save_xml_dir=save_dir)






