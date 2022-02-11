# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import random
from JoTools.utils.FileOperationUtil import FileOperationUtil

img_dir = r"D:\data\001_fzc_优化相关资料\dataset_fzc\001_train_data_step_1.5\jieya\zd"
save_dir = r"C:\Users\14271\Desktop\train_vit\3"


# for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg', '.JPG']):
#
#     random_num = random.randrange(1, 1000)
#
#     print(random_num)
#
#     if random_num > 250:
#         os.remove(each_img_path)



img_path_list =  list(FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg', '.JPG']))

FileOperationUtil.move_file_to_folder(img_path_list, save_dir, is_clicp=True)

