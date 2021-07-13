# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import matplotlib.pyplot as plt
from JoTools.txkjRes.deteRes import DeteRes

img_path = r"C:\Users\14271\Desktop\del\kkx_demo\test.jpg"
xml_path = r"C:\Users\14271\Desktop\del\kkx_demo\test.xml"

a = DeteRes()
a.xml_path = xml_path
a.img_path = img_path


print(a.get_id_list())

print(type(a.get_dete_obj_by_id(0)))
aa = a.get_sub_img_by_id(0)

print(type(a.get_dete_obj_by_id(1)))
bb = a.get_sub_img_by_id(1)

print(type(a.get_dete_obj_by_id(2)))
cc = a.get_sub_img_by_id(2, RGB=False, assign_shape_min=1000)
# cc = a.get_sub_img_by_id(2, RGB=True)


# print(aa.shape)
# print(bb.shape)
# print(cc.shape)

plt.imshow(cc)
plt.show()