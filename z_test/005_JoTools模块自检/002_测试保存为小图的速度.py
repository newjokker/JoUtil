# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import time
from JoTools.txkjRes.deteRes import DeteRes


img_path = r"C:\Users\14271\Desktop\del\test.jpg"
xml_path = r"C:\Users\14271\Desktop\del\test.xml"
save_dir = r"C:\Users\14271\Desktop\del\crop"

a = DeteRes(xml_path)

a.img_path = img_path

a.crop_dete_obj(save_dir)

# a.save_to_xml(r"C:\Users\14271\Desktop\del\crop.xml")

json_str = a.save_to_json()

b = DeteRes(json_dict=json_str)

# print()
b.save_to_xml(r"C:\Users\14271\Desktop\del\crop.xml")

c = DeteRes(r"C:\Users\14271\Desktop\del\crop.xml")

c.crop_dete_obj(save_dir)

for each_dete_obj in a:

    sub_img = a.get_sub_img_by_dete_obj_from_crop(each_dete_obj)

    print(sub_img.shape)




