# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.deteRes import DeteRes

xml_path = r"C:\Users\14271\Desktop\del\del\110kV德七Ⅰ回_0塔头 (1).xml"
a = DeteRes(xml_path=xml_path)


a.redis_conn_info=('192.168.3.185', 6379)
a.img_redis_key='image'

a.crop_and_save(r"C:\Users\14271\Desktop\del\res")
