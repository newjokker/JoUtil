# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil


img_dir = r"C:\Users\14271\Desktop\样板间测试\result_old"
save_dir = r"C:\Users\14271\Desktop\样板间测试\K_result"

new_img_xml_path_list = []

for each_xml_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.xml']):

    a = DeteRes(each_xml_path)
    if a.has_tag("K"):
        each_img_path = each_xml_path[:-4] + ".jpg"
        if os.path.exists(each_img_path):

            new_img_xml_path_list.append(each_xml_path)
            new_img_xml_path_list.append(each_img_path)


FileOperationUtil.move_file_to_folder(new_img_xml_path_list, save_dir)













