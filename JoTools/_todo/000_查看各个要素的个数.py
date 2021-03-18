# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.operateDeteRes import OperateDeteRes


xml_dir = r"C:\data\fzc_优化相关资料\000_等待训练\Annotations"

a = OperateDeteRes.get_class_count(xml_dir)

for each in a.items():
    print(each)
