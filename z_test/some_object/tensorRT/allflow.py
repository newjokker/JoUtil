# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import time
import subprocess
import argparse



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
# ----------------------------------------------------------------------------------------------------------------------

pid_list = []

cmd_str = r"python ./fwd.py --rtmp {0} --w {1} --h {2} --fps {3} --port {4}".format(rtmp, w, h, fps, port)
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



print("* use ctrl + c stop APP")

while True:

    try:
        time.sleep(1)
    except KeyboardInterrupt as e:
        # 当接受到 ctrl + c 命令，关掉启动的两个子模型
        print("* ctrl + c , close : {0}".format(','.join(pid_list)))
        #
        for each_pid in pid_list:
            os.system("kill -9 {0}".format(each_pid))
        #
        exit()






























