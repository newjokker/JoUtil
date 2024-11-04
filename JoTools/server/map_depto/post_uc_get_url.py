# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.utils.JsonUtil import JsonUtil
from JoTools.utils.TxtUtil import TxtUtil

ucd_path = r"\\192.168.3.80\数据\root_dir\uc_dataset_customer\ldq\jb3gg.json"
save_txt_path = r"C:\Users\14271\Desktop\input.txt"


a = JsonUtil.load_data_from_json_file(ucd_path)

uc_url_list = []
for each_uc in a["uc_list"]:
    uc_url_list.append([f"http://192.168.3.111:11101/file/{each_uc}.jpg\n"])


TxtUtil.write_table_to_txt(uc_url_list, save_txt_path)

