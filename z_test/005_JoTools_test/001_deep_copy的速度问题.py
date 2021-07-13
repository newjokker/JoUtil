# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import time
from JoTools.txkjRes.deteRes import DeteRes


img_path = r"C:\Users\14271\Desktop\del\test.jpg"
xml_path = r"C:\Users\14271\Desktop\del\test.xml"


a = DeteRes(xml_path)

a.img_path = img_path


a.draw_dete_res(r"C:\Users\14271\Desktop\del\draw_res_a.jpg")


# # b = a.deep_copy()
#
# c = DeteRes(json_dict=a.save_to_json())
#
# res = c.deep_copy()
#
# res.print_as_fzc_format()
# print('-'*50)
# a.print_as_fzc_format()
#
# print(a.img.width)
# print(a.img.height)
#
# print(res.img.width)
# print(res.img.height)
#
# print(a.img_path)
# print(res.img_path)
#
# for each in res:
#     if each in a:
#         print("in")
#     else:
#         print("out")
#
# # a.crop_and_save(r"C:\Users\14271\Desktop\del\crop")
#
# # res.img = a.img
# res.crop_and_save(r"C:\Users\14271\Desktop\del\crop")

# res.draw_dete_res(r"C:\Users\14271\Desktop\del\draw_res.jpg")
# res.save_to_xml(r"C:\Users\14271\Desktop\del\draw_res.xml")





