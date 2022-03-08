# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import socket
import struct
import uuid
import numpy as np
import time
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
sign_dir = r"/home/tensorRT/tensorrt_test/sign"

# fixme 目前会提是显示的图片的大小和接受的实际数据大小不一致，所以会摆错


def dete_error():
    """检测失败，发出失败的信号"""
    sign_txt = os.path.join(sign_dir, 'restart.txt')
    with open(sign_txt, 'w') as sign_file:
        sign_file.write("error")


class FrameCal():

    def __init__(self, length):
        self.length = length
        self.time_list = []

    def tag(self):
        if len(self.time_list) == self.length:
            self.time_list.pop(0)
        self.time_list.append(time.time())

    def get_frame(self):
        if len(self.time_list) <= 1:
            return -1
        else:
            start = self.time_list[0]
            end = self.time_list[-1]
            if start == end:
                return -1
            else:
                return (len(self.time_list) -1)/(time.time() - self.time_list[0])

    def get_length(self):
        return len(self.time_list)


def socket_service_image(args):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # s.bind(('0.0.0.0', 1211))
        s.bind((args.host, args.port))
        s.listen(10000)                                                                     # fixme 这边是设置的监听的时间
    except socket.error as msg:
        print(msg)
        sys.exit(1)

    print("Wait for Connection.....................")

    while True:
        sock, addr = s.accept()
        deal_image(sock, addr)


def deal_image(sock, addr):
    # print("Accept connection from {0}".format(addr))                                                # 查看发送端的ip和端口

    while True:
        fileinfo_size = struct.calcsize('128sq')
        buf = sock.recv(fileinfo_size)
        if buf:

            try:
                filename, filesize = struct.unpack('128sq', buf)
                # fn = filename.decode().strip('\x00')                                                      # file name
            except Exception as e:
                print(e)
                print(e.__traceback__.tb_frame.f_globals["__file__"])
                print(e.__traceback__.tb_lineno)
                print("restart server")
                dete_error()
                continue

            recvd_size = 0
            res = b""
            buff_size = 100 

            while not recvd_size >= filesize:
                if filesize - recvd_size > buff_size:
                    data = sock.recv(buff_size)
                    recvd_size += len(data)
                    res += data
                else:
                    data = sock.recv(buff_size)
                    recvd_size = filesize
                    res += data

            now_frame = fc.get_frame()
            if now_frame > video_fps:
                continue

            img_np_arr = np.fromstring(res, np.uint8)
            frame = cv2.imdecode(img_np_arr, cv2.COLOR_BGR2RGB)

            # ----------------------------------------------------------------------------------------------------------
            
            try:
                dete_res = model.detectSOUT(image=frame)
                # dete_res.print_as_fzc_format()
                dete_res.draw_dete_res(save_path=None, assign_img=frame, color_dict={"warning":[0,0,255], "normal":[0,255,0]})
                #
                p.stdin.write(frame.tostring())
            except Exception as e:
                print(e)
                print(e.__traceback__.tb_frame.f_globals["__file__"])
                print(e.__traceback__.tb_lineno)
                print("restart server")
                dete_error()

            fc.tag()

        sock.close()
        break


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', dest='port', type=int, default=1211)
    parser.add_argument('--host', dest='host', type=str, default='0.0.0.0')
    parser.add_argument('--rtmp', dest='rtmp', type=str, default='rtmp://192.168.3.99/123/221')
    parser.add_argument('--w', dest='w', type=int, default=1280)
    parser.add_argument('--h', dest='h', type=int, default=720)
    parser.add_argument('--fps', dest='fps', type=int, default=15)
    #
    parser.add_argument('--gpuID', dest='gpuID', type=int, default=0)
    parser.add_argument('--gpuRatio', dest='gpuRatio', type=float, default=0.1)
    parser.add_argument('--logID', dest='logID', type=str, default='0')
    parser.add_argument('--objName', dest='objName', type=str, default='')
    #
    args = parser.parse_args()
    return args



if __name__ == '__main__':

    args = parse_args()
    # ------------------------------------------------------------------------------------------------------------------
    fc = FrameCal(100)
    objName = "yolov5_rt_aqm"
    scriptName = "aqm"
    #
    # rtmp = "rtmp://192.168.3.99/123/221"
    # w, h = 1280, 720
    # video_fps = 15
    rtmp = args.rtmp
    w, h = args.w, args.h
    video_fps = args.fps
    gpuID = args.gpuID
    os.environ['CUDA_VISIBLE_DEVICES'] = str(gpuID)
    # ------------------------------------------------------------------------------------------------------------------

    start_time = time.time()
    portNum = args.port
    host = args.host
    # ------------------------------------------------------------------------------------------------------------------
    model = Yolov5RT(args, objName, scriptName)
    model.model_restore()
    # --------------------------------------------------------
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
               rtmp]

    # 管道配置
    p = sp.Popen(command, stdin=sp.PIPE)
    #
    socket_service_image(args)





