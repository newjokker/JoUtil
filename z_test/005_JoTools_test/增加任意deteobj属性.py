# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from  JoTools.txkjRes.deteRes import DeteObj, DeteRes

xml_path = r"C:\Users\14271\Desktop\del\del\0a4dd4915abc8d675ce190eef87e38ca.xml"
save_path = r"C:\Users\14271\Desktop\del.xml"

a = DeteRes()
a.add_obj(10,20,30,40, "test", 0.5)
a[0].hehe = 'just test'
a[0].add_new = 123222121
a[0].add_123 = '111122'
a.save_to_xml(save_path)


b = a.save_to_json()

a = DeteRes(json_dict=b)

print(a[0].__dict__)

print(a[0].add_123)





