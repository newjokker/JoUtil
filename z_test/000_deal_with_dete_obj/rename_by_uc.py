# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
import pymysql
import shutil
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.JsonUtil import JsonUtil

database_path   = r"\\192.168.3.80\数据\root_dir\json_img"
uc_xml_dir      = r"\\192.168.3.80\算法-数据交互\国网安监比赛数据交互\天池数据1k\广州比赛1k\审核修改\合"
save_xml_dir    = r"C:\Users\14271\Desktop\安全带\res_xml"


for each_xml_path in FileOperationUtil.re_all_file(uc_xml_dir, endswitch=[".xml"]):
    uc = FileOperationUtil.bang_path(each_xml_path)[1]

    print(uc)

    json_path = os.path.join(database_path, uc[:3], uc + ".json")

    if not os.path.exists(json_path):
        print("未找到对应 json 文件 : ", json_path)

    json_info = JsonUtil.load_data_from_json_file(json_path)
    origin_name = json_info["org_name"]
    save_path = os.path.join(save_xml_dir, origin_name[:-4] + ".xml")
    shutil.copy(each_xml_path, save_path)







