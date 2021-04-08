# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.deteRes import DeteRes
from PIL import Image

xml_path = r"C:\Users\14271\Desktop\del\del\110kV德七Ⅰ回_0塔头 (1).xml"
dete_res = DeteRes(xml_path=xml_path)


a = DeteRes()
a.redis_conn_info=('192.168.3.185', 6379)
a.img_redis_key = '123'

for each_dete_res in dete_res:
    a.add_obj_2(each_dete_res)


# a.img = Image.open(r"C:\Users\14271\Desktop\del\del\110kV德七Ⅰ回_0塔头 (1).jpg")
# a.set_img_to_redis('123')
#
# a.img = None
# a.img_redis_key='123'


# a.crop_and_save(r"C:\Users\14271\Desktop\del\res", assign_img_name="jokker_new")

c = a.deep_copy()

a.crop_and_save(r"C:\Users\14271\Desktop\del\res", assign_img_name="jokker_new")
print('-'*30)
c.crop_and_save(r"C:\Users\14271\Desktop\del\res", assign_img_name="jokker_new")
