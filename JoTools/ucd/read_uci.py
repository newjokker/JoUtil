# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.utils.JsonUtil import JsonUtil



uci_path = r"C:\Users\14271\Desktop\del\prebase_1103.uci"
obi_path = r"C:\Users\14271\Desktop\del\prebase_1103.obi"


uci = JsonUtil.load_data_from_json_file(uci_path)
obi = JsonUtil.load_data_from_json_file(obi_path)

print(uci.keys())

print(len(uci["uc_list"]))

uc = uci["uc_list"][0]

print(obi["shapes"][uc])


