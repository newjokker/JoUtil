# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.operateDeteRes import OperateDeteRes
from JoTools.utils.JsonUtil import JsonUtil
import prettytable

standard_dir = r"C:\data\fzc_优化相关资料\防振锤优化\000_标准分类测试集\crop_add_broken"
customer_dir = r"C:\Users\14271\Desktop\fzc分类验证结果\fzc_test_res_006"

# OperateDeteRes.cal_acc_classify(standard_dir, customer_dir)
label_list = ["yt", "sm", "gt", "zd_yt", "fzc_broken"]


# todo 解析 json 文件，对比每一个类型在 各个模型上的正确率和召回率

model_dir = r"C:\Users\14271\Desktop\003_test_res"
model_list = FileOperationUtil.re_all_file(model_dir, lambda x:str(x).endswith('.json'))

all_res = {}

for each_json_path in model_list:
    epoch_num = int(each_json_path.split('_')[-2])
    js_file = JsonUtil.load_data_from_json_file(each_json_path)

    each_res = {'rec':{}, 'acc':{}}
    for each in js_file:
        type_str, label, val = each[0], each[1], each[3]
        each_res[type_str][label] = val

    all_res[epoch_num] = each_res


epoch_num_list = list(all_res.keys())
epoch_num_list.sort()

tb = prettytable.PrettyTable()
# 增加标题
tb.add_column("  ", ["acc"]*len(label_list) + ["rec"]*len(label_list))
tb.add_column("  ", label_list*2)

for each_epoch in epoch_num_list:
    each_res = all_res[each_epoch]
    one_column = []

    # 增加 acc
    for each_label in label_list:
        one_column.append(each_res['acc'][each_label])
    # 增加 rec
    for each_label in label_list:
        one_column.append(each_res['rec'][each_label])

    # 增加列
    tb.add_column(str(each_epoch), one_column)

print(tb)