# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import requests
import json
import os
import argparse
import time
from JoTools.txkjRes.detectionResult import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil

# from JoTools.detectionResult import DeteRes
# from JoTools.utils.FileOperationUtil import FileOperationUtil

# todo 通用测试代码


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Tensorflow Faster R-CNN demo')
    parser.add_argument('--port', dest='port', type=int, default=7654)
    parser.add_argument('--host', dest='host', type=str, default='127.0.0.1')
    assign_args = parser.parse_args()
    return assign_args



if __name__ == "__main__":

    start_time = time.time()
    args = parse_args()
    portNum = args.port

    # ------------------------------------------------------------------------------------------
    model_name = "kkxTC"
    save_dir = r"./result"
    img_dir = input("输入要测试的文件夹地址: ")
    # ------------------------------------------------------------------------------------------

    print("-" * 100)

    url = 'http://127.0.0.1:' + str(portNum) + '//' + model_name


    for each_img_path in FileOperationUtil.re_all_file(img_dir, lambda x:str(x).endswith((".jpg", ".JPG"))):
        each_img_name = os.path.split(each_img_path)[1]
        files = {'image': open(each_img_path, 'rb')}
        data = {'filename': each_img_name}
        res = requests.post(url=url, data=data, files=files)
        #
        if res.status_code == 200:
            res = json.loads(res.text)
            #
            print('-'*50)
            print(each_img_path)
            for alarm_index, each in enumerate(res["alarms"]):
                print(" * {0}, {1}".format(alarm_index, each))

            a = DeteRes(assign_img_path=each_img_path)
            #
            # fixme 返回的要是个字典
            # if isinstance(res, dict):
            for each_obj in res['alarms']:
                position = each_obj['position']
                a.add_obj(position[0], position[1], position[0] + position[2], position[1] + position[3],
                          tag=each_obj['class'], conf=float(each_obj['possibility']))
            # else:
            #     # fixme 返回的要是个元组
            #     for each_obj in res:
            #         position = res[2:5]
            #         a.add_obj(position[0], position[1], position[2], position[3],
            #                   tag=each_obj[0], conf=float(each_obj[-1]))

            #
            a.save_to_xml(os.path.join(save_dir, os.path.split(each_img_name)[1][:-3] + 'xml'))
            # 有结果才进行保存
            if len(a.alarms) > 0:
                a.draw_dete_res(os.path.join(save_dir, os.path.split(each_img_name)[1]))
        else:
            print("error")


    end_time = time.time()
    costTime = end_time - start_time
