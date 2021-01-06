# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.deteRes import DeteRes
from JoTools.txkjRes.classifyRes import ClassifyResBase



img_path = r"C:\Users\14271\Desktop\del\img_xml\test.jpg"
xml_path = r"C:\Users\14271\Desktop\del\img_xml\test.xml"
json_path = r"C:\Users\14271\Desktop\del\img_xml\test.json"

# a = ClassifyResBase(assign_img_path=img_path, xml_path=xml_path)
a = DeteRes(assign_img_path=img_path, xml_path=xml_path)
# a.format_check()

# print(a.tag)

# a.save_to_json(json_path)
a.save_to_xml(r"C:\Users\14271\Desktop\del\img_xml\test_2.xml")



