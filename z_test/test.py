# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.txkj.parseXml import parse_xml
from JoTools.operateResXml import OperateResXml
from JoTools.detectionResult import OperateDeteRes, DeteRes
from JoTools.for_csdn.word_pic.word_pic import WordImage
from PIL import Image

xml_path = r"C:\Users\14271\Desktop\del\test.xml"
img_path = r"C:\Users\14271\Desktop\del\test.jpg"

a = DeteRes(xml_path, assign_img_path=img_path)
# a.do_nms(0.1, ignore_tag=True)
# a.filter_by_conf(0.90)
# a.filter_by_area(10000)
# a.filter_by_tages(remove_tag=["K", "Lm"])
a.filter_by_tages(need_tag=["KG"])


for each in a.count_tags().items():
    print(each)


# a.draw_dete_res(r"C:\Users\14271\Desktop\del\draw_res_nms.jpg")

