# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.txkj.parseXml import parse_xml
from JoTools.operateResXml import OperateResXml
from JoTools.detectionResult import OperateDeteRes, DeteRes
from JoTools.for_csdn.word_pic.word_pic import WordImage
from PIL import Image

xml_path = r"C:\Users\14271\Desktop\del\test.xml"
img_path = r"C:\Users\14271\Desktop\del\test.jpg"

xml_dir = r"C:\Users\14271\Desktop\优化开口销第二步\015_增加新的标图，内蒙乌海_110kV黄地Ⅱ线_110kV黄明线\kkx_xml_prepare"
# a = DeteRes(xml_path, assign_img_path=img_path)
# # a.do_nms(0.1, ignore_tag=True)
# # a.filter_by_conf(0.90)
# # a.filter_by_area(10000)
# # a.filter_by_tages(remove_tag=["K", "Lm"])
# a.filter_by_tages(need_tag=["KG"])
#
#
# for each in a.count_tags().items():
#     print(each)



# OperateDeteRes.get_area_speard(xml_dir=xml_dir)

# a.draw_dete_res(r"C:\Users\14271\Desktop\del\draw_res_nms.jpg")

a = DeteRes(
    r"C:\Users\14271\Desktop\del\crop\test.xml" ,
    assign_img_path=r"C:\Users\14271\Desktop\del\crop\test.jpg")

a.save_assign_range([10, 100, 500, 500], r"C:\Users\14271\Desktop\cut_test", save_name='res_001', iou_1=0.5)
a.save_assign_range([50, 0, 500, 500], r"C:\Users\14271\Desktop\cut_test", save_name='res_002', iou_1=0.5)
a.save_assign_range([0, 50, 1000, 1000], r"C:\Users\14271\Desktop\cut_test", save_name='res_003', iou_1=0.5)
a.save_assign_range([300, 250, 1200, 1000], r"C:\Users\14271\Desktop\cut_test", save_name='res_004', iou_1=0.5)
a.save_assign_range([500, 500, 1000, 1000], r"C:\Users\14271\Desktop\cut_test", save_name='res_005', iou_1=0.5)
a.save_assign_range([0, 500, 1000, 1300], r"C:\Users\14271\Desktop\cut_test", save_name='res_006', iou_1=0.5)
