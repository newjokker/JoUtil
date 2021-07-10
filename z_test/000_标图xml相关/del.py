# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes, DeteObj, DeteAngleObj


img_dir = r"/home/suanfa-3/ldq/002_test_res/fzc_v1.2.5.2_check_error"
save_dir = r"/home/suanfa-3/ldq/002_test_res/fzc_v1.2.5.2_check_error_crop"

index = 0

for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.xml']):
    index += 1
    try:
        a = DeteRes(each_img_path)
        print(index, a.img_path)
        a.crop_and_save(save_dir, split_by_tag=True)
    except Exception as e:
        print(e)

#     img_name = img_name.split('-+-')[0]
#
#     img_name_set.add(img_name)
#
#
# with open(r"C:\data\fzc_优化相关资料\dataset_fzc\000_0_标准测试集\000_wuhan_20k\fzc_broken.txt", 'w') as txt_file:
#     for each in img_name_set:
#         txt_file.write("{0}.jpg\n".format(each))

# img_dir = r"/home/suanfa-1/ceshiji"
# save_dir =r"/home/suanfa-3/ldq/002_test_res/del/fzc_broken_img"
#
# img_path_list = []
#
# with open(r"/home/suanfa-3/ldq/002_test_res/del/fzc_broken.txt", 'r') as txt_file:
#     for each_img_name in txt_file:
#         each_img_name = each_img_name.strip()
#         each_img_path = os.path.join(img_dir, each_img_name)
#         if os.path.exists(each_img_path):
#             img_path_list.append(each_img_path)
#
# FileOperationUtil.move_file_to_folder(img_path_list, save_dir, is_clicp=False)
#
#


