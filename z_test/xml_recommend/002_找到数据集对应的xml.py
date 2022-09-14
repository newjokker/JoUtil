# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.utils.JsonUtil import JsonUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil

json_path = r"C:\Users\14271\Desktop\xml_recommend\prebase_extra.json"
xml_dir = r"C:\Users\14271\Desktop\xml_recommend\Annonations"
save_dir = r"C:\Users\14271\Desktop\xml_recommend\Annonations_extra"

xml_path_list = []
a = JsonUtil.load_data_from_json_file(json_path)
for each_uc in a["uc_list"]:
    each_uc_path = os.path.join(xml_dir, each_uc + ".xml")
    xml_path_list.append(each_uc_path)
    print(each_uc)

FileOperationUtil.move_file_to_folder(xml_path_list, save_dir, is_clicp=False)



