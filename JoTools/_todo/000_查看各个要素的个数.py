# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.operateDeteRes import OperateDeteRes



xml_dir = r"C:\Users\14271\Desktop\fzc_train_new\xml_new"

a = OperateDeteRes.get_class_count(xml_dir)

for each in a.items():
    print(each)
