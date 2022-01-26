# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.utils.CsvUtil import CsvUtil
from JoTools.utils.TxtUtil import TxtUtil
from JoTools.utils.JsonUtil import JsonUtil
import zhconv

a = CsvUtil.read_csv_to_list(r"C:\Users\14271\Desktop\成语词典\dict_idioms_2020_20211229（2）.csv")


cy_list = []
cy_json_list = []
for each in a:
    print(each[3])
    cy_list.append([zhconv.convert(each[1], 'zh-hans') + ',' + each[3] + '\n'])
    cy_json_list.append(zhconv.convert(each[1], 'zh-hans'))

print(len(a))


JsonUtil.save_data_to_json_file(cy_json_list, r"chengyuzidian.json")


TxtUtil.write_table_to_txt(cy_list, r"chengyu.txt")
#
