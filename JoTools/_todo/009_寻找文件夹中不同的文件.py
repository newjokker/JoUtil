# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.utils.FileOperationUtil import FileOperationUtil


crop_old_dir = r"C:\Users\14271\Desktop\fzc_train_new\crop_old"
crop_new_dir = r"C:\Users\14271\Desktop\fzc_train_new\crop_new"


res = FileOperationUtil.find_diff_file(
    FileOperationUtil.re_all_file(crop_old_dir, lambda x:str(x).endswith('.jpg')),
    FileOperationUtil.re_all_file(crop_new_dir, lambda x:str(x).endswith('.jpg'))
)


print(len(res['inanotb']))
print(len(res['inbnota']))

FileOperationUtil.move_file_to_folder(res['inanotb'], r"C:\Users\14271\Desktop\fzc_train_new\diff_crop", is_clicp=False)


# print(res)
print("ok")