# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import requests
import prettytable
# from flask import Flask, request, jsonify
import json

"""
* 测试模型训练是否可用
"""


# ---------------------------------------------------- 训练 ------------------------------------------------------------

# url = 'http://192.168.3.110:8084/training/'
url = r'http://192.168.3.155:3232/record_find'

def show_find_res(find_res):
    """展示查找的结果"""
    tb = prettytable.PrettyTable()
    tb.field_names = ['index', 'command']
    for each in sorted(find_res, key=lambda x:x[0]):
        tb.add_row(each)
    print(tb)


while True:

    command_info = input("CM:")

    d = {
        "command_info":command_info,
    }

    r = requests.post(url, data=d)

    res = json.loads(r.text)["res"]

    if res:
        show_find_res(res)

