# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.utils.FileOperationUtil import FileOperationUtil


class A(FileOperationUtil):

    def b(self):
        pass

c = A.b
print(c.__dict__)


# file_dir = r"C:\Users\14271\anaconda3\Lib\site-packages\JoTools\utils"
#
# print(A.b.__module__)
#
#
# for each_file_path in FileOperationUtil.re_all_file(file_dir, endswitch=['.py']):
#
#     file_info = FileOper3.ationUtil.get_file_describe_dict(each_file_path)
#     print(FileOperationUtil.bang_path(each_file_path)[1], file_info)
#
