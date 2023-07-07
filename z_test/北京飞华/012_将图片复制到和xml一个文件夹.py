# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import shutil
from JoTools.utils.FileOperationUtil import FileOperationUtil
# from JoTools.utils.PickleUtil import PickleUtil

img_dir     = r"/home/ldq/beijingfeihua/010_验电签字/img_dir"
xml_dir     = r"/home/ldq/beijingfeihua/010_验电签字/img_dir_dete"
pkl_path    = r"./name_dict.pkl"


name_dict = {}

for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=[".jpg"]):
    img_name = FileOperationUtil.bang_path(each_img_path)[1]
    name_dict[img_name] = each_img_path

# PickleUtil.save_data_to_pickle_file(name_dict, pkl_path)
# name_dict = PickleUtil.load_data_from_pickle_file(pkl_path)

for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=[".xml"]):
    xml_name = FileOperationUtil.bang_path(each_xml_path)[1]

    if xml_name in name_dict:
        save_img_path = os.path.join(xml_dir, xml_name + ".jpg")
        shutil.move(name_dict[xml_name], save_img_path)
        print("success : ", xml_name)
    else:
        print("error : ", xml_name)















