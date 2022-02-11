# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import time
import numpy as np
import argparse
import cv2
import json
from gevent import monkey
from gevent.pywsgi import WSGIServer
monkey.patch_all()
from flask import Flask, request, jsonify
import threading
import configparser
import ctypes
import gc
import os, sys
import subprocess
import subprocess as sp

this_dir = os.path.dirname(__file__)
lib_path = os.path.join(this_dir, '..')
sys.path.insert(0, lib_path)

from lib.detect_libs.yolov5RT import Yolov5RT
from JoTools.utils.FileOperationUtil import FileOperationUtil

# --------------------------------------
sys.path.insert(0, r"/home/tensorRT/tensorrtx/yolov5")
PLUGIN_LIBRARY = "/home/tensorRT/tensorrtx/yolov5/build/libmyplugins.so"
ctypes.CDLL(PLUGIN_LIBRARY)


# todo 推送和计算是在一边进行的，另外一边做的是图像截取和推送操作



app = Flask(__name__)


@app.route('/test', methods=['POST'])
def demo():
    top = 200
    base64_code = request.files['image'].stream.read()
    img_np_arr = np.fromstring(base64_code, np.uint8)
    im = cv2.imdecode(img_np_arr, cv2.COLOR_BGR2RGB)
    # 控制存储结构的长度
    stack.append(im)
    if len(stack) > top:
        del stack[:50]
        gc.collect()
    # 检测
    frame = stack.pop()
    dete_res = model.detectSOUT(image=frame)
    dete_res.print_as_fzc_format()
    #
    p.stdin.write(frame.tostring())
    # p.stdin.write(frame.tobytes())
    #
    return jsonify({"length": len(stack)})


def serv_start():
    global host, portNum
    http_server = WSGIServer((host, portNum), app)
    http_server.serve_forever()


def parse_args():
    parser = argparse.ArgumentParser(description='Tensorflow Faster R-CNN demo')
    parser.add_argument('--gpuID', dest='gpuID', type=int, default=0)
    parser.add_argument('--port', dest='port', type=int, default=5444)
    parser.add_argument('--gpuRatio', dest='gpuRatio', type=float, default=0.1)
    parser.add_argument('--host', dest='host', type=str, default='127.0.0.1')
    parser.add_argument('--logID', dest='logID', type=str, default='0')
    parser.add_argument('--objName', dest='objName', type=str, default='')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    stack = []

    start_time = time.time()
    args = parse_args()
    # portNum = args.port
    # host = args.host
    portNum = 1211
    host = "0.0.0.0"

    objName = "yolov5_rt_aqm"
    scriptName = "aqm"
    # --------------------------------------------------------
    model = Yolov5RT(args, objName, scriptName)
    model.model_restore()
    # --------------------------------------------------------
    # rtmpUrl = "rtsp://192.168.3.221/live"
    rtmpUrl = "rtmp://192.168.3.99/123/221"
    w, h = 1280, 720
    video_fps = 5
    # -----
    command = ['ffmpeg',
               '-y',
               '-f', 'rawvideo',
               '-vcodec', 'rawvideo',
               '-pix_fmt', 'bgr24',
               '-thread_queue_size', '512',
               '-s', "{}x{}".format(w, h),
               '-r', str(video_fps),
               '-i', '-',
               '-c:v', 'libx264',
               '-pix_fmt', 'yuv420p',
               '-preset', 'ultrafast',
               '-tune', 'zerolatency',
               '-sc_threshold', '499',
               '-rtsp_transport', 'tcp',
               '-f', 'rtsp',
               rtmpUrl]

    # 管道配置
    p = sp.Popen(command, stdin=sp.PIPE)

    #
    serv_start()





