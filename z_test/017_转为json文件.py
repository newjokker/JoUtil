# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.deteRes import DeteRes
from JoTools.txkjRes.classifyRes import ClassifyResBase
from JoTools.utils.JsonUtil import JsonUtil


img_path = r"C:\Users\14271\Desktop\del\img_xml\test.jpg"
xml_path = r"C:\Users\14271\Desktop\del\img_xml\test.xml"
json_path = r"C:\Users\14271\Desktop\del\img_xml\test.json"

# a = ClassifyResBase(assign_img_path=img_path, xml_path=xml_path)
# a = DeteRes(assign_img_path=img_path, xml_path=xml_path)
a = DeteRes(assign_img_path=img_path)
# a = DeteRes(assign_img_path=img_path, json_dict=json_path)

# b = DeteRes(json_dict=a.save_to_json())

# a.format_check()

# print(a.tag)

# print(b.alarms)

# a.save_to_json(json_path)
# a.save_to_xml(r"C:\Users\14271\Desktop\del\img_xml\test_2.xml")


json_dict = a.save_to_json()

print(json_dict)

print(type(json_dict))

b = DeteRes(json_dict=json_dict)

print(b.save_to_json())

JsonUtil.save_data_to_json_file(json_dict, r"C:\Users\14271\Desktop\del\img_xml\123.json")

for each in b.do_fzc_format():
    print(each)