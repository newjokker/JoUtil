# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
import prettytable
import os, sys

this_dir = os.path.dirname(__file__)
lib_path = os.path.join(this_dir, '..')
sys.path.insert(0, lib_path)

import numpy as np
import argparse
import cv2
from gevent import monkey
from gevent.pywsgi import WSGIServer
import datetime

monkey.patch_all()
from flask import Flask, request, jsonify
import threading
import configparser
app = Flask(__name__)




class RecordFind():
    """记录和查找"""

    def __init__(self):
        self.records = {}
        self.index = 0
        self.save_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), r'./data.txt')
        self.load()

    def find(self, assign_record_list):
        """查找"""
        # fixme 支持两种模式，一个是并集查找，一个是交集查找
        res = []
        for each_index in self.records:
            for each_record in assign_record_list:
                if each_record in self.records[each_index]:
                    res.append((each_index, self.records[each_index]))
                    break
        return res

    def save(self):
        """保存"""
        with open(self.save_path, "w") as txt_file:
            for each_line in self.records:
                txt_file.write(self.records[each_line])
                txt_file.write('\n')

    def load(self):
        """加载"""
        if not os.path.exists(self.save_path):
            return

        self.index = 0
        with open(self.save_path, "r") as txt_file:
            for each_line in txt_file:
                self.index += 1
                self.records[self.index] = each_line.strip()

    def add(self, assign_record):
        """增加"""
        self.index += 1
        self.records[self.index] = assign_record

    def show_record(self):
        """打印展示"""
        # 按照 index 从小到大排序

        for each in self.records:
            print(each)

    def del_by_index(self, assign_index):
        """删除"""
        assign_index = int(assign_index.strip())
        if assign_index in self.records:
            del self.records[assign_index]
        else:
            print("no index : {0}".format(assign_index))

    def refresh(self):
        """刷新，序号重排，保存文件"""
        # 保存
        self.save()
        # 读取
        self.load()

def parse_command(command_str):
    """解析命令"""

    command_str = " ".join(str(command_str).split()).strip()

    if command_str.startswith("find"):
        # 查找命令
        command_str = command_str[4:].strip().split(" ")
        if command_str != ['']:
            res = a.find(command_str)
            # show_find_res(res)
            return res
        else:
            print("command error")
    elif command_str.startswith("add"):
        # 增加命令
        command_str = command_str[3:].strip()
        a.add(command_str)
    elif command_str.startswith("del"):
        # 删除命令
        command_str = command_str[3:].strip()
        a.del_by_index(command_str)
    elif command_str.startswith("save"):
        a.save()
    elif command_str.startswith("refresh"):
        a.refresh()
    else:
        print("command str need start with add or find or del")

def show_find_res(find_res):
    """展示查找的结果"""
    tb = prettytable.PrettyTable()
    tb.field_names = ['index', 'command']
    for each in sorted(find_res, key=lambda x:x[0]):
        tb.add_row(each)
    print(tb)

# ----------------------------------------------------------------------------------------------------------------------

@app.route('/record_find', methods=['POST'])
def demo():

    command_info = request.form['command_info']
    res = parse_command(command_info)
    rsp = {'res': res}
    return jsonify(rsp)

def serv_start():
    global host, portNum
    http_server = WSGIServer((host, portNum), app)
    http_server.serve_forever()

def parse_args():
    parser = argparse.ArgumentParser(description='Tensorflow Faster R-CNN demo')
    parser.add_argument('--port', dest='port', type=int, default=3232)
    parser.add_argument('--host', dest='host', type=str, default='192.168.3.155')   # 这边要是写 127 的话只能在本服务器访问了，要改为本机的地址
    args = parser.parse_args()
    return args


if __name__ == "__main__":


    args = parse_args()
    portNum = args.port
    host = args.host

    url = r"http://" + host + ":" +  str(portNum) + "/record_find"
    print(url)

    # ----------------------------------------------------------------------------------

    a = RecordFind()
    serv_start()










