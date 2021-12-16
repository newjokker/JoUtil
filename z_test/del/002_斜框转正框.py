# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes


xml_dir = r"C:\Users\14271\Desktop\连接件训练\xml_angle"
save_dir = r"C:\Users\14271\Desktop\连接件训练\xml"
img_dir = r"E:\连接件训练数据集"


for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):
    a = DeteRes(xml_path=each_xml_path)
    a.img_path = os.path.join(img_dir, os.path.split(each_xml_path)[1][:-4]+'.jpg')
    a.angle_obj_to_obj()
    # a.save_to_xml(os.path.join(save_dir, os.path.split(each_xml_path)[1]))
    a.draw_dete_res(os.path.join(r"C:\Users\14271\Desktop\连接件训练\img", os.path.split(each_xml_path)[1][:-4]+'.jpg'))

