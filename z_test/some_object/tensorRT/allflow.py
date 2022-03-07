# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import time
import subprocess
import argparse

# fixme 指定要启动的 GPU

def parse_args():
    parser = argparse.ArgumentParser(description='Tensorflow Faster R-CNN demo')
    parser.add_argument('--port', dest='port', type=int, default=1211)
    parser.add_argument('--host', dest='host', type=str, default='127.0.0.1')
    parser.add_argument('--fps', dest='fps', type=str, default=15)
    parser.add_argument('--w', dest='w', type=int, default=1280)
    parser.add_argument('--h', dest='h', type=int, default=720)
    parser.add_argument('--rtsp', dest='rtsp', type=str, default=r"rtsp://admin:txkj@2021!@192.168.3.19:554/Streaming/Channels/101")
    parser.add_argument('--rtmp', dest='rtmp', type=str, default=r"rtsp://192.168.3.99/live/1211")
    parser.add_argument('--log_dir', dest='log_dir', type=str, default=r"./logs")
    parser.add_argument('--gpuID', dest='gpuID', type=int, default=0)
    args = parser.parse_args()
    return args

# ----------------------------------------------------------------------------------------------------------------------
args = parse_args()
log_dir = args.log_dir
host = args.host
port = args.port
rtsp = args.rtsp
rtmp = args.rtmp
w, h = args.w, args.h
fps = args.fps
gpuID = args.gpuID
# ----------------------------------------------------------------------------------------------------------------------

try:
    # 实时获取视频长宽的大小，传给服务端
    import cv2
    cap = cv2.VideoCapture(rtsp)
    w, h = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
except Exception as e:
    print(e)


def start_servre():
    pid_list = []
    cmd_str = r"python ./fwd.py --rtmp {0} --w {1} --h {2} --fps {3} --port {4} --gpuID {5}".format(rtmp, w, h, fps, port, gpuID)
    bug_file = open(os.path.join(log_dir, "bug_server" + str(time.time())[:10] + ".txt"), "w+")
    std_file = open(os.path.join(log_dir, "std_server" + str(time.time())[:10] + ".txt"), "w+")
    print(cmd_str)
    pid = subprocess.Popen(cmd_str.split(), stdout=std_file, stderr=bug_file, shell=False)
    pid_list.append(str(pid.pid))
    print("* start cilent pid : ", pid.pid)

    time.sleep(10)

    cmd_str = r"python ./khd_rtsp.py --host {0} --port {1} --rtsp {2}".format(host, port, rtsp)
    bug_file = open(os.path.join(log_dir, "bug_cilent" + str(time.time())[:10] + ".txt"), "w+")
    std_file = open(os.path.join(log_dir, "std_cilent" + str(time.time())[:10] + ".txt"), "w+")
    print(cmd_str)
    pid = subprocess.Popen(cmd_str.split(), stdout=std_file, stderr=bug_file, shell=False)
    pid_list.append(str(pid.pid))
    print("* start server pid : ", pid.pid)
    return pid_list

def close_all_server(pid_list):
    for each_pid in pid_list:
        os.system("kill -9 {0}".format(each_pid))

pid_list = start_servre()
print("* use ctrl + c stop APP")

while True:
    start_time = time.time()
    try:
        # todo 过一段时间就重启一下两个服务，保证常新
        time.sleep(1)
        now_time = time.time()
        if now_time - start_time > 60 * 60 * 5:
            start_time = time.time()
            close_all_server(pid_list)
            pid_list = start_servre()
    except KeyboardInterrupt as e:
        # 当接受到 ctrl + c 命令，关掉启动的两个子模型
        print("* ctrl + c , close : {0}".format(','.join(pid_list)))
        close_all_server(pid_list)
        exit()






























