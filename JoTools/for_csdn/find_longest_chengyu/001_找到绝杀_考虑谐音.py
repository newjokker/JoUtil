# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# todo 两个字典 （1）最难接上的成语

from JoTools.utils.JsonUtil import JsonUtil
from JoTools.utils.CsvUtil import CsvUtil
from pypinyin import pinyin, Style
import pypinyin


a = JsonUtil.load_data_from_json_file(r"chengyuzidian.json")

# #普通模式
# print(pinyin('中心', style=Style.NORMAL))

def chinese2pingyin(chinese):
    res = []
    a = pinyin(chinese, style=Style.NORMAL)
    for each in a:
        res.append(each[0])
    return res



# 最好接的字
head_cy_head = {}                                    # 代表的是每一个字被对上的概率大小
head_cy_tail = {}                                    # 代表的是每一个字被对上的概率大小
word_hard_index_head = {}
word_hard_index_tail = {}
for each in a:
    each = chinese2pingyin(each)
    if each[0] in head_cy_head:
        head_cy_head[each[0]].append(each)
    else:
        head_cy_head[each[0]] = [each]
    #
    if each[-1] in head_cy_tail:
        head_cy_tail[each[-1]].append(each)
    else:
        head_cy_tail[each[-1]] = [each]


for each in head_cy_head:
    word_hard_index_head[each] = len(head_cy_head[each])
# JsonUtil.save_data_to_json_file(word_hard_index_head, r"word_hard_index_head.json")

for each in head_cy_tail:
    word_hard_index_tail[each] = len(head_cy_tail[each])
# JsonUtil.save_data_to_json_file(word_hard_index_tail, r"word_hard_index_tail.json")



# 计算每一个成语的接上的概率和被接上的概率，算作入度和出度，就能计算出来成语的需要背上的指数
important_index = {}

important_index_list = []
important_index_list.append(["each_cy", "pingyin", "input_index", "output_index"])

for each_chinese in a:

    each_cy = each_chinese
    each_cy = chinese2pingyin(each_cy)

    head, tail = each_cy[0], each_cy[-1]
    #
    if head not in word_hard_index_tail:
        input_index = 0
    else:
        input_index = word_hard_index_tail[head]
    #
    if tail not in word_hard_index_head:
        output_index = 0
    else:
        output_index = word_hard_index_head[tail]
    #
    important_index_list.append([each_chinese, each_cy, input_index, output_index])


CsvUtil.save_list_to_csv(important_index_list, r"important_index.csv")









