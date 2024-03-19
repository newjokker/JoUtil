# -*- coding: utf-8  -*-
# -*- author: jokker -*-

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
    img_path = os.path.join(img_dir, image_name)
    if os.path.exists(img_path):
        with open(img_path, 'rb') as f:
            image = f.read()
            resp = Response(image, mimetype="image/png")
            return resp
    else:
        print(f"* no such img path : {img_path}")

@app.route('/save', methods=['post'])
def save_img_to_map_depot():
    """将图片存入图床"""
    try:
        base64_code = request.files['image'].stream.read()
        img_np_arr = np.fromstring(base64_code, np.uint8)
        im = cv2.imdecode(img_np_arr, cv2.COLOR_BGR2RGB)
        md5 = HashLibUtil.get_str_md5(im)
        save_path = os.path.join(img_dir, md5 + '.jpg')
        if not os.path.exists(save_path):
            print(save_path)
            cv2.imencode('.jpg', im)[1].tofile(save_path)
        else:
            print("* image exists")
        return jsonify({'status': 'success', 'url': f'http://{ip}:{port}/image/{md5}.jpg'}), 200
    except Exception as e:
        print(e)
        print(e.__traceback__.tb_frame.f_globals["__file__"])
        print(e.__traceback__.tb_lineno)
        return jsonify({'status': 'failed'}), 200

def parse_args():
    parser = argparse.ArgumentParser(description='map depto')
    parser.add_argument('--port', dest='port', type=int, default=8000)
    parser.add_argument('--host', dest='host', type=str, default='0.0.0.0')
    parser.add_argument('--img_dir', dest='img_dir', default=r"C:\Users\14271\Desktop\del\mapdepot\imgs", type=str)
    parser.add_argument('--ip', dest='ip', type=str, default='192.168.4.175')
    #
    args = parser.parse_args()
    return args

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

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
    img_dir = args.img_dir      # 存储图片的文件夹
    host = args.host            # 0.0.0.0
    port = args.port            # 对外的端口号
    ip = get_ip()               # 本机的 ip

    print_config()

    serv_start()

