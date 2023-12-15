# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.operateDeteRes import OperateDeteRes


xml_dir = r"\\192.168.3.80\算法-数据交互\杆塔缺螺栓-横担螺栓定位标注\new_tag"
region_img_dir = r"F:\输电基础前置数据\二批次\JPEGImages2"
save_xml_dir = r"C:\Users\14271\Desktop\res_xml"


OperateDeteRes.get_xml_from_crop_xml(xml_dir, region_img_dir, save_xml_dir)
