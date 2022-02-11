# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import configparser
import gc
import os, sys
import subprocess
from multiprocessing import Process, Queue, Manager
import multiprocessing
import cv2
import time
import torch
import argparse
import numpy as np
from scripts.drawbox import inference

this_dir = os.path.dirname(__file__)
lib_path = os.path.join(this_dir, '..')
sys.path.insert(0, lib_path)
import threading
from gevent import monkey
from gevent.pywsgi import WSGIServer
import torch

# torch.set_num_threads(10)
monkey.patch_all()
from flask import Flask, request, jsonify
from lib.detect_libs.YanHuoDetection import yanhuoDetection
from lib.detect_utils.timer import Timer


class MyThread(threading.Thread):
    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args
        self.result = self.func(*self.args)

    def get_result(self):
        # 必须等待线程执行完毕,如果线程还未执行完毕就去获取result是没有结果的
        threading.Thread.join(self)
        try:
            return self.result
        except Exception:
            return None


def demo(stack):
    video_source = args.input_stream
    print(video_source)
    top = 200
    time.sleep(5)
    cap = cv2.VideoCapture(video_source)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    # ret, frame = video_capture.read()
    while True:
        ret, frame = cap.read()
        if ret:
            stack.append(frame)
            if len(stack) >= top:
                # print('Stack is full.........')
                del stack[:50]
                gc.collect()                                    # 增加垃圾回收装置


def realse(stack):
    args = parse_args()
    cap = cv2.VideoCapture(args.input_stream)
    fps = cap.get(cv2.CAP_PROP_FPS)
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    rtmpUrl = args.output_stream
    command = ['ffmpeg',
               '-y',
               '-f', 'rawvideo',
               '-vcodec', 'rawvideo',
               '-pix_fmt', 'bgr24',
               '-thread_queue_size', '512',
               '-s', "{}x{}".format(size[0], size[1]),
               '-r', str(fps),
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
    p = subprocess.Popen(command, stdin=subprocess.PIPE)
    fps_time = 0
    f = 0
    count = 0
    while True:
        f += 1

        if len(stack) > 0:
            frame = stack.pop()
            # image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            # frame = image
            name = str(f) + '.jpg'
            voc_labels = model.detect(frame, name)
            MYLOG.info("detect result: \n {}".format(voc_labels))
            objects = {}
            results = model.postProcess(frame, voc_labels)
            objects['yanhuo_demo'] = results
            alarms = inference(MYLOG, frame, name, objects, True)
            if cv2.waitKey(1) & 0xff == ord('q'):
                break
            rsp = {scriptName: results}
            p.stdin.write(frame.tostring())
    cap.release()
    p.terminate()
    cv2.destroyAllWindows()


def parse_args():
    parser = argparse.ArgumentParser(description='Tensorflow Faster R-CNN demo')
    parser.add_argument('--gpuID', dest='gpuID', type=int, default=1)
    parser.add_argument('--port', dest='port', type=int, default=7662)
    parser.add_argument('--gpuRatio', dest='gpuRatio', type=float, default=0.3)
    parser.add_argument('--host', dest='host', type=str, default='0.0.0.0')
    parser.add_argument('--logID', dest='logID', type=str, default='0')
    parser.add_argument('--objName', dest='objName', type=str, default='yh')
    parser.add_argument('--input_stream', dest='input_stream', type=str, default='rtsp://admin:txkj@2021!@192.168.3.19:554/h264/ch1/main/av_stream')
    parser.add_argument('--output_stream', dest='output_stream', type=str, default='rtsp://192.168.3.202/live/cs4')
    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = parse_args()
    portNum = args.port
    host = args.host
    # objName = args.objName
    workdir = os.path.dirname(os.path.abspath(__file__))
    CONFIG_PATH = os.path.join(workdir, "config.ini")
    TMP_DIR = os.path.join(workdir, 'tmpfiles')
    LOG_DIR = os.path.join(workdir, 'logs')
    os.chdir(workdir)
    cf = configparser.ConfigParser()
    cf.read(CONFIG_PATH)

    # ------------------------------------------------------------------------------------------------------------------
    objName = cf.get('common', 'model')
    scriptName = os.path.basename(__file__).split('.')[0]
    model = yanhuoDetection(args, objName, scriptName)
    # ------------------------------------------------------------------------------------------------------------------

    resizedImgPath = model.getTmpPath('yh')
    MYLOG = model.log
    MYLOG.info("=" * 20 + objName + "=" * 20)
    t = Manager().list()

    t1 = Process(target=demo, args=(t,))
    t2 = Process(target=realse, args=(t,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

