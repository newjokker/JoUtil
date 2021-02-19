# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.utils.FileOperationUtil import FileOperationUtil


root_dir_1 = r"C:\Users\14271\Desktop\del\test001"
root_dir_2 = r"C:\Users\14271\Desktop\del\test002"

FileOperationUtil.merge_root_dir(root_dir_1, root_dir_2, is_clip=True)