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
from JoTools.txkj.jsonInfo import JsonInfo


monkey.patch_all()

app=Flask(__name__)


# todo 一次性后台起多个，这样就不用一个个启动了

# todo windows 上 nginx 的使用


@app.route("/image/<uc_suffix>")
def get_image(uc_suffix):
    # 图片上传保存的路径
    img_path = os.path.join(img_dir, uc_suffix[:3], uc_suffix)
    print(img_path)
    if os.path.exists(img_path):
        with open(img_path, 'rb') as f:
            image = f.read()
            # refer : https://tool.oschina.net/commons/_contenttype.dea
            resp = Response(image, mimetype="image/jpeg")
            return resp
    else:
        print(f"* no such img path : {img_path}")

@app.route("/json/<uc_suffix>")
def get_json(uc_suffix):
    # 图片上传保存的路径
    json_path = os.path.join(img_dir, uc_suffix[:3], uc_suffix)
    print(json_path)
    if os.path.exists(json_path):
        with open(json_path, 'rb') as f:
            json_file = f.read()
            resp = Response(json_file, mimetype="application/x-javascript")
            return resp
    else:
        print(f"* no such json path : {json_path}")

@app.route("/xml/<uc_suffix>")
def get_xml(uc_suffix):
    # 图片上传保存的路径
    json_path = os.path.join(img_dir, uc_suffix[:3], uc_suffix[:-4] + ".json")
    if os.path.exists(json_path):
        json_info = JsonInfo(json_path=json_path)
        save_xml_path = os.path.join(tmp_dir, uc_suffix)
        json_info.save_to_xml(xml_path=save_xml_path)
        print(save_xml_path)
        with open(save_xml_path, 'rb') as f:
            xml_file = f.read()
            resp = Response(xml_file, mimetype="text/xml")
            # os.remove(save_xml_path)
            return resp
    else:
        print(f"* no such json path : {json_path}")


def parse_args():
    parser = argparse.ArgumentParser(description='map depto')
    parser.add_argument('--port', dest='port', type=int, default=3232)
    parser.add_argument('--host', dest='host', type=str, default='0.0.0.0')
    parser.add_argument('--img_dir', dest='img_dir', type=str)
    parser.add_argument('--tmp_dir', dest='tmp_dir', type=str, default=r"/tmp")
    parser.add_argument('--ip', dest='ip', type=str)
    #
    args = parser.parse_args()
    return args

def print_config():
    print("-"*30)
    print(f'host : {host}')
    print(f'port : {port}')
    print(f'ip : {ip}')
    print(f'img_dir : {img_dir}')
    print(f'tmp_dir : {tmp_dir}')
    print("-"*30)


def serv_start():
    global host, port
    http_server = WSGIServer((host, port), app)
    http_server.serve_forever()


if __name__ == '__main__':


    #
    args = parse_args()
    img_dir = r"\\192.168.3.80\数据\root_dir\json_img"
    tmp_dir = args.tmp_dir
    host = args.host
    port = args.port
    ip = args.ip

    print_config()

    serv_start()
