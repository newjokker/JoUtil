

import os
import random
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.RandomUtil import RandomUtil

img_dir = r"C:\Users\jokker\Desktop\del\fzc\img"
xml_dir = r"C:\Users\jokker\Desktop\del\fzc\xml"
save_xml_dir = r"C:\Users\jokker\Desktop\del\fzc\res\xml"
save_img_dir = r"C:\Users\jokker\Desktop\del\fzc\res\img"

need_tags = ['040303022']
index_count = 10

# ----------------------------------------------------------------------------------------------------------------------


all_img_path_list = FileOperationUtil.re_all_file(img_dir, lambda x: str(x).endswith(('.jpg', '.JPG')))

xml_path_list = []
img_path_list = []

index = 0
for each_img_path in all_img_path_list:
    each_img_name = os.path.split(each_img_path)[1]
    each_xml_path = os.path.join(xml_dir, each_img_name[:-3] + 'xml')

    a = DeteRes()
    a.xml_path = each_xml_path

    for each_obj in a.alarms:
        if each_obj.tag in need_tags:
            xml_path_list.append(each_xml_path)
            img_path_list.append(each_img_path)
            index += 1
            break

    if index > index_count:
        break

FileOperationUtil.move_file_to_folder(xml_path_list, save_xml_dir, is_clicp=False)
FileOperationUtil.move_file_to_folder(img_path_list, save_img_dir, is_clicp=False)






