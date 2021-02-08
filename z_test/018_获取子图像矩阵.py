# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.deteRes import DeteRes

img_path = r"C:\Users\14271\Desktop\del\img_xml\test.jpg"
xml_path = r"C:\Users\14271\Desktop\del\img_xml\test.xml"
json_path = r"C:\Users\14271\Desktop\del\img_xml\test.json"

# a = ClassifyResBase(assign_img_path=img_path, xml_path=xml_path)
a = DeteRes(assign_img_path=img_path, xml_path=xml_path)


for each in a.get_fzc_format():
    print(each)

each_img = a.get_sub_img_by_id(0)
print(each_img)
