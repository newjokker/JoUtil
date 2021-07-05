# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
from JoTools.utils.FileOperationUtil import FileOperationUtil



img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\JPEGImages"
xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\Annotations_broken"

need_move_xml_list = []

for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):
    each_img_path = os.path.join(img_dir, FileOperationUtil.bang_path(each_xml_path)[1] + '.jpg')

    if not os.path.exists(each_img_path):
        need_move_xml_list.append(each_xml_path)



FileOperationUtil.move_file_to_folder(need_move_xml_list, r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\999.找到的重复的数据", is_clicp= True)








