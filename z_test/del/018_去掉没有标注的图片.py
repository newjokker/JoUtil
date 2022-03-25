# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.utils.FileOperationUtil import FileOperationUtil



json_dir = r"C:\Users\14271\Desktop\xj_train\003_统一标签\annotations"
img_dir = r"C:\Users\14271\Desktop\xj_train\002_数据汇总"
save_dir = r"C:\Users\14271\Desktop\xj_train\003_统一标签\JPEGImages"


# a = FileOperationUtil.re_all_file_list(json_dir)[:10]
a = FileOperationUtil.re_all_folder_list(json_dir)[:10]

print(a)



# save_img_path_list = []
# for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg', '.png', '.PNG', '.JPG']):
#     _, img_name, _ = FileOperationUtil.bang_path(each_img_path)
#     json_path = os.path.join(json_dir, img_name + '.json')
#
#     if os.path.exists(json_path):
#         save_img_path_list.append(each_img_path)
#     else:
#         print(json_path)
#
#
# FileOperationUtil.move_file_to_folder(save_img_path_list, save_dir, is_clicp=False)

