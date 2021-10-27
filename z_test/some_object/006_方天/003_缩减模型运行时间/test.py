# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.utils.TxtUtil import TxtUtil


file_path = r"C:\Users\14271\Desktop\del\use_time_analysis.txt"

a = TxtUtil.read_as_tableread_as_table(file_path)

use_time_dict = {}

for each in a:

    model_name, use_time = each[0].split(":")

    model_name = model_name.strip()
    use_time = use_time.strip()

    if model_name in use_time_dict:
        use_time_dict[model_name] += float(use_time)
    else:
        use_time_dict[model_name] = float(use_time)


for each in use_time_dict.items():
    print(each)



