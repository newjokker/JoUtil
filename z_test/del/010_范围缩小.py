# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from  JoTools.txkjRes.deteRes import DeteRes
from JoTools.txkjRes.deteObj import DeteObj

img_path = r"C:\Users\14271\Desktop\del\del\00fa186e8d4d6660b49ddef8a35a77de.jpg"
xml_path = r"C:\Users\14271\Desktop\del\del\00fa186e8d4d6660b49ddef8a35a77de.xml"

a = DeteRes(xml_path=xml_path, assign_img_path=img_path)




a.add_obj(500, 500, 1000, 1000, 'test', '0')


for each_obj in a.deep_copy():
    new_each_obj = each_obj.deep_copy()
    new_each_obj.do_augment([-0.2,-0.2,-0.3,-0.3], a.width, a.height, is_relative=True)
    a.add_obj_2(new_each_obj)



a.draw_dete_res(r"C:\Users\14271\Desktop\tensorrt_test_new.jpg")




