# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
import shutil
from JoTools.utils.FileOperationUtil import FileOperationUtil


# 找到成对的 xml 和 img

xml_dir = r"C:\Users\14271\Desktop\jyzps_new_xml"
img_dir = r"C:\Users\14271\Desktop\jyzps_new_xml"
save_dir = r"C:\Users\14271\Desktop\res"


move_img_list = []
for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg', '.JPG', '.png', '.PNG']):
    each_xml_path = os.path.join(xml_dir, FileOperationUtil.bang_path(each_img_path)[1] + '.xml')

    if os.path.exists(each_xml_path):
        move_img_list.append(each_img_path)
        move_img_list.append(each_xml_path)

FileOperationUtil.move_file_to_folder(move_img_list, save_dir, is_clicp=False)












