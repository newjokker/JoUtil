# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.PrintUtil import PrintUtil
# todo 添加移动的记录，这样方便数据的还原

region_img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\JPEGImages"
region_xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_train_data_step_1\Annotations"
new_img_dir = r"C:\Users\14271\Desktop\wuhan_006_fzc\JPEGImages"
new_xml_dir = r"C:\Users\14271\Desktop\wuhan_006_fzc\Annotations"

new_xml_path_list = []
new_img_path_list = []

index = 0
for each_img_path in FileOperationUtil.re_all_file(new_img_dir, endswitch=['.jpg', '.JPG', '.png', '.PNG']):
    # print(index, each_img_path)
    index += 1
    each_xml_path = os.path.join(new_xml_dir, FileOperationUtil.bang_path(each_img_path)[1] + '.xml')
    #
    each_new_img_path = os.path.join(region_img_dir, os.path.split(each_img_path)[1])
    each_new_xml_path = os.path.join(region_xml_dir, os.path.split(each_xml_path)[1])

    if os.path.exists(each_new_img_path):
        print("* img path exists : {0}".format(each_new_img_path))
        continue

    if os.path.exists(each_new_xml_path):
        print("* xml path exists : {0}".format(each_new_xml_path))
        continue

    new_img_path_list.append(each_img_path)
    new_xml_path_list.append(each_xml_path)


PrintUtil.print(new_img_path_list)
print('-'*30)
PrintUtil.print(new_xml_path_list)

FileOperationUtil.move_file_to_folder(new_img_path_list, region_img_dir, is_clicp=True)
FileOperationUtil.move_file_to_folder(new_xml_path_list, region_xml_dir, is_clicp=True)






