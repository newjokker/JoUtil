# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.deteRes import DeteRes



img_path = r"C:\Users\14271\Desktop\del\test\00fa186e8d4d6660b49ddef8a35a77de.jpg"
xml_path = r"C:\Users\14271\Desktop\del\test\save.xml"
save_xml_path = r"C:\Users\14271\Desktop\del\test\save_002.xml"

a = DeteRes(xml_path=xml_path, assign_img_path=img_path)


print(a.des)


a.des = "just test 003"


b = a.save_to_json()

c = DeteRes(json_dict=b)

c.print_as_fzc_format()

c.save_to_xml(save_xml_path)











