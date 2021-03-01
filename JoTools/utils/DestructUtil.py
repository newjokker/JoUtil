# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import time
from functools import wraps


# TODO 运行 n 次之后，对指定的文件进行删除

# 在 util.py 文件创建一个隐藏文件，里面是 json 或者 pkl 文件，记录一个字典，某个文件可以运行几次，最终执行多少次就需要进行删除


import os
import shutil
from JoTools.utils.JsonUtil import JsonUtil


abs_path = os.path.abspath(__file__)
abs_dir = os.path.dirname(abs_path)


file_path = os.path.join(abs_dir, '.destruct.json')


def destruct_file_after_times(assign_file_path, assign_times):
    """在运行执行指定次数之后删除制定文件或者文件夹"""

    del_count = 'del_count'
    now_count = 'now_count'

    # 读取文件信息
    if os.path.exists(file_path):
        file_dict = JsonUtil.load_data_from_json_file(file_path)
    else:
        file_dict = {}
    # 缓存文件
    if not os.path.exists(assign_file_path):
        return
    # 可以执行次数的字典
    if assign_file_path not in file_dict:
        file_dict[assign_file_path] = {del_count: assign_times, now_count: 1}
    else:
        file_dict[assign_file_path][now_count] += 1
    # 判断文件是否要进行删除
    if file_dict[assign_file_path][now_count] >= file_dict[assign_file_path][del_count]:
        shutil.rmtree(assign_file_path)
    # 保存缓存文件
    JsonUtil.save_data_to_json_file(file_dict, file_path)
    # 返回还可以执行的次数
    return file_dict[assign_file_path][del_count] - file_dict[assign_file_path][now_count]










# def print_path():
#     print(abs_path)
#     print(abs_dir)
#     print(os.getcwd())
#     print(__file__)
#













