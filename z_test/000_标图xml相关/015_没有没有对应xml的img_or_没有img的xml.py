# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.PrintUtil import PrintUtil

img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\JPEGImages"
xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\xml_fix"
save_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\001_找到没有img的xml，重新标"

lonely_img_path_list = []
lonely_xml_path_list = []
empty_xml_path_list = []

lonely_xml_dir = os.path.join(save_dir, 'loney_xml')
lonely_img_dir = os.path.join(save_dir, 'loney_img')
empty_xml_dir = os.path.join(save_dir, 'empty_xml')
os.makedirs(lonely_img_dir, exist_ok=True)
os.makedirs(lonely_xml_dir, exist_ok=True)
os.makedirs(empty_xml_dir, exist_ok=True)


for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):
    each_img_path = os.path.join(img_dir, FileOperationUtil.bang_path(each_xml_path)[1] + '.jpg')

    if not os.path.exists(each_img_path):
        lonely_xml_path_list.append(each_xml_path)
    else:
        a = DeteRes(each_xml_path)

        if len(a) < 1:
            empty_xml_path_list.append(each_xml_path)

#
for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg', '.JPG', '.png', '.PNG']):
    each_xml_path = os.path.join(xml_dir, FileOperationUtil.bang_path(each_img_path)[1] + '.xml')

    if not os.path.exists(each_xml_path):
        lonely_img_path_list.append(each_img_path)

print('-'*50)
# for each in lonely_img_path_list:
PrintUtil.print(lonely_xml_path_list)
print('-'*50)
PrintUtil.print(lonely_img_path_list)
print('-'*50)
PrintUtil.print(empty_xml_path_list)


FileOperationUtil.move_file_to_folder(lonely_xml_path_list, lonely_xml_dir, is_clicp=True)
FileOperationUtil.move_file_to_folder(lonely_img_path_list, lonely_img_dir, is_clicp=True)
FileOperationUtil.move_file_to_folder(empty_xml_path_list, empty_xml_dir, is_clicp=True)


