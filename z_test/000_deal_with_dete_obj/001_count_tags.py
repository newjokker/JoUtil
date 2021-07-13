# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.operateDeteRes import OperateDeteRes


# xml_dir = r"C:\Users\14271\Desktop\002_test_res_0.6"
xml_dir = r"C:\Users\14271\Desktop\寻找未被发现的fzc_broken\train_data\Annotations"

OperateDeteRes.get_class_count(xml_dir, print_count=True)
