# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import matplotlib.pyplot as plt
from JoTools.txkjRes.deteRes import DeteRes

img_path = r"C:\Users\14271\Desktop\del\kkx_demo\test.jpg"
xml_path = r"C:\Users\14271\Desktop\del\kkx_demo\test.xml"

a = DeteRes()
a.xml_path = xml_path
a.img_path = img_path


a.print_as_fzc_format()


obj_list = a.get_dete_obj_list_by_func(lambda x: 'K' in x.tag, is_deep_copy=True)

for each in obj_list:
    # each.tag = 'test'
    print(each.tag)

# a.print_as_fzc_format()




