# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# 给所有的入库图片创建一个图床

import os
import cv2
import numpy as np
import socket
import requests
import argparse
from flask import Flask, Response, request, jsonify
from JoTools.utils.HashlibUtil import HashLibUtil
from gevent import monkey
from gevent.pywsgi import WSGIServer
monkey.patch_all()

app=Flask(__name__)


@app.route("/image/<image_name>")
def get_frame(image_name):
    # 图片上传保存的路径
    img_path = os.path.join(img_dir, image_name[:3], image_name)
    print(img_path)
    if os.path.exists(img_path):
        with open(img_path, 'rb') as f:
            image = f.read()
            resp = Response(image, mimetype="image/png")
            return resp
    else:
        print(f"* no such img path : {img_path}")


def parse_args():
    parser = argparse.ArgumentParser(description='map depto')
    parser.add_argument('--port', dest='port', type=int, default=3232)
    parser.add_argument('--host', dest='host', type=str, default='0.0.0.0')
    parser.add_argument('--img_dir', dest='img_dir', type=str)
    parser.add_argument('--ip', dest='ip', type=str, default='192.168.3.221')
    #
    args = parser.parse_args()
    return args

def print_config():
    print("-"*30)
    print(f'host : {host}')
    print(f'port : {port}')
    print(f'ip : {ip}')
    print("-"*30)


def serv_start():
    global host, port
    http_server = WSGIServer((host, port), app)
    http_server.serve_forever()


if __name__ == '__main__':


    #
    args = parse_args()
    img_dir = r"\\192.168.3.80\数据\root_dir\json_img"
    host = args.host
    port = args.port
    ip = args.ip

    print_config()

    serv_start()
