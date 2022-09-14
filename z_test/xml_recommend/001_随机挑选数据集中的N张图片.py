# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import json
import random
from JoTools.utils.JsonUtil import JsonUtil

json_path = r"C:\Users\14271\Desktop\xml_recommend\prebase_all.json"



a = JsonUtil.load_data_from_json_file(json_path)

uc_list = a["uc_list"]

random.seed(34)

# uc_list = list(set(uc_list))
# random.shuffle(uc_list)

a["uc_list"] = uc_list[:2000]
JsonUtil.save_data_to_json_file(a, r"C:\Users\14271\Desktop\xml_recommend\prebase_base.json")

a["uc_list"] = uc_list[2000:3000]
JsonUtil.save_data_to_json_file(a, r"C:\Users\14271\Desktop\xml_recommend\prebase_random.json")

a["uc_list"] = uc_list[2000:]
JsonUtil.save_data_to_json_file(a, r"C:\Users\14271\Desktop\xml_recommend\prebase_extra.json")

print(uc_list[:10])











