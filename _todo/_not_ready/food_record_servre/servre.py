# -*- coding: utf-8  -*-
# -*- author: jokker -*-

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


class ServerDemo():

    def print(self):
        return "ok"

class EatInfo():
    """一次饮食信息"""

    # 类似格式 今天|昨天|前天|20201023 早饭 | 鸡蛋 3  3.5| 玉米 2 | 红薯 1 |  20圆   ps 吃的还不错的
    # 用  | 符号间隔每一个种类中的信息，里面可以有 1 到 3 个参数，A 鸡蛋 B 鸡蛋 3 C 鸡蛋 3 3.5 ，split | 然后中间的就是每一炖吃的东西
    # 必须要有时间信息，如果第一个参数不是正常的时间参数信息，会直接问是不是今天吃的
    # 需要有 一天中的哪一顿 的信息，通过关键字解析得到

    def __init__(self):
        self.eat_date = None    # 默认为当天日期
        self.eat_time = None    # 早，中，晚，夜宵，其他
        self.one_meal_info = {"date":None, "time":None, "food_info":[], "price":None, "ps":None}

    def check_format(self, eat_str):
        """输入数据的格式检查"""
        return True

    def _get_food_info(self, food_info_str):
        """获取食物信息"""
        food_info_list = []
        # 解析一顿饭的信息
        for each_str in food_info_str:
            each_info = {"num":-1, "class":None, "price":-1}
            each_str = str(each_str).strip().split(" ")
            if len(each_str) == 1:
                each_info["class"] = each_str[0]
            elif len(each_str) == 2:
                each_info["class"] = each_str[0]
                each_info["num"] = each_str[1]
            elif len(each_str) == 3:
                each_info["class"] = each_str[0]
                each_info["num"] = each_str[1]
                each_info["price"] = each_str[2]
            else:
                print("不符合规范 --> {0}".format(each_str))

            food_info_list.append(each_info)

        self.one_meal_info['food_info'] = food_info_list

    def _get_other_info(self, other_info_str):
        """获得其他信息"""

        other_info_list = " ".join(other_info_str.split()).split(" ")

        # 解析信息
        for index, each in enumerate(other_info_list):
            # 获取价格信息
            if  each.endswith(("圆", "Y", "元")):
                # 获取总价
                if each[:-1].isdigit():
                    self.one_meal_info["price"] = float(each[:-1])
            # 获取 ps 信息
            elif each == "ps" or each == "PS":
                if len(other_info_list) >= index + 2:
                    self.one_meal_info["ps"] = other_info_list[index + 1]
            # 指定准确的日期
            elif len(each) == 8 and each.isdigit():
                self.one_meal_info["date"] = each
            # 模糊指定
            elif each in ["今天", "昨天","前天"]:
                lt = datetime.datetime.now()
                timedelta_dict = {"今天":0, "昨天":-1, "前天":-2}
                lt += datetime.timedelta(days=timedelta_dict[each])
                self.one_meal_info["date"] = datetime.datetime.strftime(lt, "%Y%m%d")
            # 吃饭时间
            elif each in ["早上", "早晨", "早", "morning", "mon"]:
                self.one_meal_info["time"] = "早餐"
            elif each in ["中午", "noon"]:
                self.one_meal_info["time"] = "午餐"
            elif each in ["晚上", "晚", "afternoon"]:
                self.one_meal_info["time"] = "晚餐"
            elif each in ["夜宵", "夜", "night"]:
                self.one_meal_info["time"] = "夜宵"

        # --------------------------------------------------------------------------------------------------------------

        if self.one_meal_info["price"] is None:
            total_price = 0
            for each_food in self.one_meal_info["food_info"]:
                print(each_food)

                if float(each_food["price"]) == -1:
                    total_price = -1
                else:
                    total_price += float(each_food["price"])

            self.one_meal_info["price"] = total_price

        # 没有解析到时间信息
        if self.one_meal_info["date"] is None:
            lt = datetime.datetime.now()
            self.one_meal_info["date"] = datetime.datetime.strftime(lt, "%Y%m%d")

    def parse_info_from_str(self, eat_info):
        """从 str 中解析信息，"""

        # eat_info = "20201023 早饭 | 鸡蛋 3  3.5| 玉米 2 | 红薯 |  20Y   ps 吃的还不错的"
        # eat_info = "早饭 | 鸡蛋 3  3.5| 玉米 2  5| 红薯 7 |  ps 吃的还不错的"

        if not self.check_format(eat_info):
            print("error ，输入不符合规范，请重新输入")
            return

        # 吃饭信息处理
        eat_info = " ".join(eat_info.split())   # 将相邻的空格进行合并，只留下一个空格
        food_info_str = eat_info.split("|")[1:-1]
        other_info_str = " ".join([eat_info.split("|")[0], eat_info.split("|")[-1]])
        # 解析食物信息
        self._get_food_info(food_info_str)
        # 解析其他信息
        self._get_other_info(other_info_str)

        return self.one_meal_info


@app.route('/demo', methods=['POST'])
def demo():

    eat_info_str = request.form['eat_info']
    res = a.parse_info_from_str(eat_info_str)
    rsp = {'res': res}
    return jsonify(rsp)


def serv_start():
    global host, portNum
    http_server = WSGIServer((host, portNum), app)
    http_server.serve_forever()


def parse_args():
    parser = argparse.ArgumentParser(description='Tensorflow Faster R-CNN demo')
    parser.add_argument('--port', dest='port', type=int, default=5444)
    parser.add_argument('--host', dest='host', type=str, default='192.168.3.155')   # 这边要是写 127 的话只能在本服务器访问了，要改为本机的地址
    args = parser.parse_args()
    return args


if __name__ == '__main__':


    # ----------------------------------------------------------------------------------
    args = parse_args()
    portNum = args.port
    host = args.host

    url = r"http://" + host + ":" +  str(portNum) + "/demo"
    print(url)
    # ----------------------------------------------------------------------------------
    a = EatInfo()
    serv_start()


