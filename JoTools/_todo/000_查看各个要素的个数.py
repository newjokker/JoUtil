# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.operateDeteRes import OperateDeteRes


xml_dir = r"D:\算法培育-7月样本\金具\保护金具\防振锤\xml"

a = OperateDeteRes.get_class_count(xml_dir)

for each in a.items():
    print(each)
