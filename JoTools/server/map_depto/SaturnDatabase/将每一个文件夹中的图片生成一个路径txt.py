# -*- coding: utf-8  -*-
# -*- author: jokker -*-
import os

from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.TxtUtil import TxtUtil


img_dir = r"\\192.168.3.80\数据\root_dir\json_img"
save_dir = r"C:\Users\14271\Desktop\del\mapdepot\uc"

for each_uc_dir in FileOperationUtil.re_all_folder(img_dir, recurse=False):
    uc_dir = os.path.split(each_uc_dir)[1]
    each_txt_path = os.path.join(save_dir, uc_dir + '.txt')

    txt_table = []
    for each_img_path in FileOperationUtil.re_all_file(each_uc_dir, endswitch=[".jpg", ".JPG", ".png", ".PNG"]):

        each_img_name = os.path.split(each_img_path)[1]

        each_url = f"http://192.168.4.175:1121/image/{each_img_name}"

        txt_table.append([each_url])

    TxtUtil.write_table_to_txt(txt_table, each_txt_path, end_line='\n')

    print(f"* save {each_txt_path} success")










