# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.operateDeteRes import OperateDeteRes

xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\Annotations"

res = OperateDeteRes.get_class_count(xml_dir)

for each in res.items():
    print(each)

# ------------------------------------------------------------------------------------------------------------
print('-'*100)

xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\Annotations_old"

res = OperateDeteRes.get_class_count(xml_dir)

for each in res.items():
    print(each)





