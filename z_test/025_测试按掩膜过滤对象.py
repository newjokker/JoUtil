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


# b = a.get_sub_img_by_id(0, assign_shape_min=1000, RGB=False)
b = a.get_sub_img_by_id(0, assign_shape_min=1000)
print(b.shape)

# b = a.get_sub_img_by_id(0)
# print(b.shape)

plt.imshow(b)
plt.show()

# a.get_sub_img_by_id(1)


# # a.draw_dete_res(r"C:\Users\14271\Desktop\res.jpg")
#
#
# xk = a.get_dete_obj_by_id(2)
#
# # Lm = a.get_dete_obj_by_id(0)
#
#
# # a.filter_by_mask(mask=xk.get_points(), cover_index_th=0.5, need_in=True)
#
#
# for each in a.get_fzc_format():
#     print(each)
#
#
# print("ok")

