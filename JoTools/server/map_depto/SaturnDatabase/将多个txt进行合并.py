# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.utils.TxtUtil import TxtUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil


uc_dir = r"C:\Users\14271\Desktop\del\mapdepot\uc"


uc_table = []
for each_txt_path in FileOperationUtil.re_all_file(uc_dir, endswitch=['.txt']):
    each_table = TxtUtil.read_as_tableread_as_table(each_txt_path)
    uc_table.extend(each_table)
    print(each_txt_path)


TxtUtil.write_table_to_txt(uc_table, r"C:\Users\14271\Desktop\del\mapdepot\uc.txt", end_line='\n')











