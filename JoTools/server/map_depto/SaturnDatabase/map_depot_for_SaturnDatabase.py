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
from JoTools.utils.FileOperationUtil import FileOperationUtil


monkey.patch_all()

app=Flask(__name__)


# todo 一次性后台起多个，这样就不用一个个启动了

# todo windows 上 nginx 的使用

# todo ucd 名字中不能有特殊字符，比如斜杠之类的


@app.route("/file/<uc_suffix>")
def get_uc_file(uc_suffix):
    # 图片上传保存的路径
    if uc_suffix.endswith(".jpg"):
        img_path = os.path.join(img_dir, uc_suffix[:3], uc_suffix)
        print(img_path)
        if os.path.exists(img_path):
            with open(img_path, 'rb') as f:
                image = f.read()
                resp = Response(image, mimetype="image/png")
                return resp
        else:
            print(f"* no such img path : {img_path}")
    elif uc_suffix.endswith(".xml"):
        xml_path = os.path.join(img_dir, uc_suffix[:3], uc_suffix[:-4] + ".json")
        if os.path.exists(xml_path):
            json_info = JsonInfo(json_path=xml_path)
            save_xml_path = os.path.join(tmp_dir, uc_suffix)
            json_info.save_to_xml(xml_path=save_xml_path)
            print(save_xml_path)
            with open(save_xml_path, 'rb') as f:
                xml_file = f.read()
                resp = Response(xml_file, mimetype="text/xml")
                return resp
        else:
            print(f"* no such json path : {xml_path}")
    elif uc_suffix.endswith(".json"):
        json_path = os.path.join(img_dir, uc_suffix[:3], uc_suffix)
        print(json_path)
        if os.path.exists(json_path):
            with open(json_path, 'rb') as f:
                json_file = f.read()
                resp = Response(json_file, mimetype="application/x-javascript")
                return resp
        else:
            print(f"* no such json path : {json_path}")

@app.route("/ucd/check")
def check_ucdataset():
    """打印所有的 ucdataset，官方的或者非官方的"""
    ucd_dict = {"official":[], "customer":[]}

    # official
    for each_ucd in FileOperationUtil.re_all_file(ucd_official_dir, endswitch=['.json']):
        # 官方 ucd 可以分为不同文件夹
        each_ucd_name = each_ucd[len(ucd_official_dir)+1:][:-5]
        ucd_dict["official"].append(each_ucd_name)

    # customer
    for each_ucd in FileOperationUtil.re_all_file(ucd_customer_dir, endswitch=['.json']):
        each_ucd_name = each_ucd[len(ucd_customer_dir)+1:][:-5]
        ucd_dict["customer"].append(each_ucd_name)
    return jsonify(ucd_dict)

@app.route("/ucd/delete/<ucd_name>", methods=["DELETE"])
def delete_ucdataset(ucd_name):
    """打印所有的 ucdataset，官方的或者非官方的"""

    ucd_path = os.path.join(ucd_customer_dir, ucd_name)
    print(ucd_path)

    if os.path.exists(ucd_path):
        os.remove(ucd_path)
        return jsonify("ok", 200)
    else:
        return jsonify("ucd path not exists", 500)

@app.route("/ucd/upload", methods=["POST"])
def upload_ucdataset():
    """打印所有的 ucdataset，官方的或者非官方的"""
    if "ucd_name" in request.form:
        ucd_name = request.form["ucd_name"]
    else:
        return jsonify("ucd_name not exists", 500)

    file = request.files['json_file']
    save_ucd_path = os.path.join(ucd_customer_dir, ucd_name + '.json')
    file.save(save_ucd_path)
    return jsonify("ok", 200)

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
    ucd_official_dir = r"\\192.168.3.80\数据\root_dir\uc_dataset"
    ucd_customer_dir = r"\\192.168.3.80\数据\root_dir\uc_dataset_customer"
    tmp_dir = args.tmp_dir
    host = args.host
    port = args.port
    ip = args.ip

    print_config()

    serv_start()
