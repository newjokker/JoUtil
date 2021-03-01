# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.operateDeteRes import OperateDeteRes



xml_dir = r"C:\Users\jokker\Desktop\del\fzc\xml"

a = OperateDeteRes.get_class_count(xml_dir)

for each in a.items():
    print(each)
