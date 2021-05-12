# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.HashlibUtil import HashLibUtil
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes



# a = OperateDeteRes.get_class_count(r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\Annotations")
# a = OperateDeteRes.get_class_count(r"C:\data\fzc_优化相关资料\000_等待训练\Annotations")
a = OperateDeteRes.get_class_count(r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\Annotations_broken")

for each in a.items():
    print(each)


# for each in FileOperationUtil.re_all_file(r"C:\data\fzc_优化相关资料\000_等待训练\Annotations", lambda x:str(x).endswith(".xml")):
#     a = DeteRes(xml_path=each)
#
#     if a.has_tag('fzc_broken'):
#         print(each)
#         break




# file_list = []
# file_list.extend(list(FileOperationUtil.re_all_file(r"C:\data\fzc_优化相关资料\000_等待训练", lambda x: str(x).endswith(('.jpg', '.JPG')))))
#
# a = HashLibUtil.duplicate_checking(file_list)
#
# for each in a:
#     print(each)


