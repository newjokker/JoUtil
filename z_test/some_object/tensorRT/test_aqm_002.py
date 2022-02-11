# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import ctypes
import configparser
import gc
import os, sys
import subprocess
from multiprocessing import Process, Manager
import multiprocessing as mp
import cv2
import time
import argparse

this_dir = os.path.dirname(__file__)
lib_path = os.path.join(this_dir, '..')
sys.path.insert(0, lib_path)

from lib.detect_libs.yolov5RT import Yolov5RT
from JoTools.utils.FileOperationUtil import FileOperationUtil

# --------------------------------------
sys.path.insert(0, r"/home/tensorRT/tensorrtx/yolov5")
PLUGIN_LIBRARY = "/home/tensorRT/tensorrtx/yolov5/build/libmyplugins.so"
ctypes.CDLL(PLUGIN_LIBRARY)

import pycuda.driver as cuda
import pycuda.autoinit
# --------------------------------------


def demo(stack):
    # video_source = args.input_stream
    video_source = "rtsp://admin:txkj-2021@192.168.3.17:554/Streaming/Channels/401"
    print(video_source)
    top = 200
    time.sleep(1)
    cap = cv2.VideoCapture(video_source)
    # cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
    while True:
        ret, frame = cap.read()
        if ret:
            stack.append(frame)
            print("* append")
            time.sleep(1)
            if len(stack) >= top:
                print('Stack is full.........')
                del stack[:50]
                gc.collect()

def realse(stack):

    import pycuda.driver as cuda
    import pycuda.autoinit

    f = 0

    while True:
        f += 1
        time.sleep(1)
        print(len(stack))
        if len(stack) > 0:
            print("* pop ")
            frame = stack.pop()
            name = str(f) + '.jpg'
            print("frame", frame.shape)
            dete_res = model.detectSOUT(image=frame)
            dete_res.print_as_fzc_format()

def parse_args():
    parser = argparse.ArgumentParser(description='Tensorflow Faster R-CNN demo')
    parser.add_argument('--gpuID', dest='gpuID', type=int, default=1)
    parser.add_argument('--port', dest='port', type=int, default=7662)
    parser.add_argument('--gpuRatio', dest='gpuRatio', type=float, default=0.3)
    parser.add_argument('--host', dest='host', type=str, default='0.0.0.0')
    parser.add_argument('--logID', dest='logID', type=str, default='0')
    parser.add_argument('--objName', dest='objName', type=str, default='yh')
    parser.add_argument('--input_stream', dest='input_stream', type=str, default='rtsp://admin:txkj-2021@192.168.3.17:554/Streaming/Channels/401')
    parser.add_argument('--output_stream', dest='output_stream', type=str, default='rtsp://192.168.3.202/live/cs4')
    args = parser.parse_args()

    return args



import threading
from pycuda import driver

# class gpuThread(threading.Thread):
#     def __init__(self, gpuid):
#         threading.Thread.__init__(self)
#         self.ctx  = driver.Device(gpuid).make_context()
#         self.device = self.ctx.get_device()
#
#     def run(self):
#         print "%s has device %s, api version %s"  \
#              % (self.getName(), self.device.name(), self.ctx.get_api_version())
#         # Profit!
#
#     def join(self):
#         self.ctx.detach()
#         threading.Thread.join(self)

driver.init()
ngpus = driver.Device.count()
for i in range(ngpus):
    t = gpuThread(i)
    t.start()
    t.join()







if __name__ == "__main__":

    args = parse_args()
    portNum = args.port
    host = args.host

    # ------------------------------------------------------------------------------------------------------------------
    objName = "yolov5_rt_aqm"
    scriptName = "aqm"
    #

    model = Yolov5RT(args, objName, scriptName)
    model.model_restore()

    # mp.set_start_method('spawn')

    # ------------------------------------------------------------------------------------------------------------------

    t = Manager().list()

    t1 = Process(target=demo, args=(t,))
    t2 = Process(target=realse, args=(t,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()












