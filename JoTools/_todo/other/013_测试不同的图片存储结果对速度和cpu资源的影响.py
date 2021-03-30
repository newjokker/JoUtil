# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import time
from JoTools.txkjRes.deteRes import DeteRes

# fixme 测试读一张大图和读取很多小图，哪一个更加消耗 io
# fixme



a = DeteRes(assign_img_path=r"C:\Users\14271\Desktop\del\del\110kV德七Ⅰ回_0塔头 (1).jpg")
# a.img_path = r"C:\Users\14271\Desktop\del\del\110kV德七Ⅰ回_0塔头 (1).jpg"
a.xml_path = r"C:\Users\14271\Desktop\del\del\110kV德七Ⅰ回_0塔头 (1).xml"
# a.refresh_obj_id()
print(a.get_id_list())
# exit()

print(a.img.width, a.img.height)

start_time = time.time()

for each in a.get_id_list():
    sub_img = a.get_sub_img_by_id(each)
    print(sub_img.shape)

print(time.time() - start_time)




