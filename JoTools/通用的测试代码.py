# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import requests
import json
import os
import argparse
import time
from .detectionResult import DeteRes
from .utils.FileOperationUtil import FileOperationUtil

def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Tensorflow Faster R-CNN demo')
    parser.add_argument('--gpuID', dest='gpuID', type=str, default='0')
    parser.add_argument('--gpuRatio', dest='gpuRatio', type=float, default=0.6)
    parser.add_argument('--gpuMemory', dest='gpuMemory', type=str, default='')
    parser.add_argument('--port', dest='port', type=int, default=7654)
    parser.add_argument('--host', dest='host', type=str, default='127.0.0.1')
    args = parser.parse_args()
    return args



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
            a.save_to_xml(os.path.join(save_dir, os.path.split(each_img_name)[1][:-3] + 'xml'))
            a.draw_dete_res(os.path.join(save_dir, os.path.split(each_img_name)[1]))

        else:
            print("error")


    end_time = time.time()
    costTime = end_time - start_time
