# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.utils.CsvUtil import CsvUtil
from JoTools.txkj.eagleUtil import EagleMetaData
from JoTools.utils.FileOperationUtil import FileOperationUtil

# todo 要强制重新加载数据库，才能将新修改的内容同步到 eagle 里面

csv_path = r"C:\Users\14271\Desktop\del\qxzd.csv"
img_dir = r"\\192.168.3.80\数据\9eagle数据库\peiyu_06.library\images"

def remove_empty_from_list(assign_list):
    res = []
    for each in assign_list:
        if each != "":
            res.append(each)
    return res

# ----------------------------------------------------------------------------------------------------------------------

a = CsvUtil.read_csv_to_list(csv_path)
code_dict = {}
for each in a:
    code_str = each[0] + "_" + "_".join(remove_empty_from_list(each[2:-1]))
    code_dict[each[0]] = code_str

# ----------------------------------------------------------------------------------------------------------------------

for index, each_json_path in enumerate(FileOperationUtil.re_all_file(img_dir, lambda x:str(x).endswith('.json'))):
    a = EagleMetaData()
    a.load_atts_from_json(each_json_path)
    print(index)

    if a.comments is not None:
        for each_comment in a.comments:
            code = each_comment['annotation'].strip()
            if code in code_dict:
                each_comment['annotation'] = code_dict[code]
            else:
                print("lose : ", each_comment['annotation'].strip())

        a.save_to_json_file(each_json_path)

print("OK")



