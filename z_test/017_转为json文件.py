# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkj.imageAugmentation import ImageAugmentation
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.detectionResult import DeteRes




xml_path = r"C:\data\kkx_退出\000_标准验证集\xml\00c07dc3-10b8-4fff-84b7-2cda4e68fa58.xml"
json_path = r"C:\Users\14271\Desktop\del\123.json"

a = DeteRes(json_path=json_path)
a.format_check()
a.save_to_xml(r"C:\Users\14271\Desktop\del\123.xml")



