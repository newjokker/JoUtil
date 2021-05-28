# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# todo TDYP-9 的所有图片跑一遍

import requests
import json
import os
import argparse
import time

from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.DecoratorUtil import DecoratorUtil


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Tensorflow Faster R-CNN demo')
    parser.add_argument('--gpuID', dest='gpuID', type=str, default='0')
    parser.add_argument('--gpuRatio', dest='gpuRatio', type=float, default=0.6)
    parser.add_argument('--gpuMemory', dest='gpuMemory', type=str, default=5000)
    parser.add_argument('--port', dest='port', type=int, default=12321)
    parser.add_argument('--host', dest='host', type=str, default='127.0.0.1')
    args = parser.parse_args()
    return args


@DecoratorUtil.time_this
def test_one_img(each_img_path):
    """测试一张图"""
    each_img_name = os.path.split(each_img_path)[1]
    files = {'image': open(each_img_path, 'rb')}
    data = {'filename': each_img_name}

    res = requests.post(url=url, data=data, files=files)
    #
    if res.status_code == 200:
        res = json.loads(res.text)
        #
        for each in res["alarms"]:
            print(" * {0}".format(each))

        a = DeteRes(assign_img_path=each_img_path)
        a.height = int(res['height'])
        a.width = int(res['width'])
        #
        # fixme 返回的要是个字典
        if isinstance(res, dict):
            for each_obj in res['alarms']:
                position = each_obj['position']
                a.add_obj(position[0], position[1], position[0] + position[2], position[1] + position[3],
                          tag=each_obj['class'], conf=float(each_obj['possibility']))
        else:
            # fixme 返回的要是个元组
            for each_obj in res:
                position = res[2:5]
                a.add_obj(position[0], position[1], position[2], position[3],
                          tag=each_obj[0], conf=float(each_obj[-1]))

        #
        # a.save_to_xml(os.path.join(save_dir, os.path.split(each_img_name)[1][:-3] + 'xml'))
        # a.draw_dete_res(os.path.join(save_dir, os.path.split(each_img_name)[1]))
        print('-' * 50)
    else:
        print(res)
        print("error")


if __name__ == "__main__":

    start_time = time.time()
    # args = parse_args()
    portNum = 11223
    model_name = "fzc"

    # save_dir = r"./result"
    # img_dir = input("输入要测试的文件夹地址: ")
    img_dir = r"D:\电科院2020算法培育.library\images"

    xml_dir = r"C:\Users\14271\Desktop\all_data_fzc\fzc_step_2_demo"
    # ------------------------------------------------------------------------------------------

    print("-" * 100)

    url = 'http://127.0.0.1:' + str(portNum) + '//' + model_name
    # url = 'http://192.168.3.155:11223/fzc'

    print(url)

    img_list = FileOperationUtil.re_all_file(img_dir, lambda x: str(x).endswith((".jpg", ".JPG")))

    for index, each_img_path in enumerate(img_list):

        # todo 判断文件名是不是在缓存文件中有，没有的话，就运行，有的话就跳过
        file_name = os.path.split(each_img_path)[1][:-3] + 'xml'
        if os.path.exists(os.path.join(xml_dir, file_name)):
            print("* check already")
            continue

        index += 1
        print(index, each_img_path)

        try:
            test_one_img(each_img_path)
        except Exception as e:
            print(e)

    end_time = time.time()
    costTime = end_time - start_time
    print('img count : ', index)
    print('cost time : ', costTime)
