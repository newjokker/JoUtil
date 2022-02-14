# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import time
import subprocess

# ----------------------------------------------------------------------------------------------------------------------
log_dir = r"./logs"
host = "192.168.3.221"
port = 1211
rtsp = r"rtsp://admin:txkj-2021@192.168.3.17:554/Streaming/Channels/501"
rtmp = r"rtmp://192.168.3.99/123/221"
w, h = 1280, 720
fps = 15
# ----------------------------------------------------------------------------------------------------------------------



cmd_str = r"python ./khd_rtsp.py --host {0} --port {1} --rtsp {2}".format(host, port, rtsp)
bug_file = open(os.path.join(log_dir, "bug_cilent" + str(time.time())[:10] + ".txt"), "w+")
std_file = open(os.path.join(log_dir, "std_cilent" + str(time.time())[:10] + ".txt"), "w+")
print(cmd_str)
pid = subprocess.Popen(cmd_str.split(), stdout=std_file, stderr=bug_file, shell=False)
print(pid.pid)

time.sleep(5)

cmd_str = r"python ./fwd --rtmp {0} --w {1} --h {2} --fps {3} --port {4}".format(rtmp, w, h, fps, port)
bug_file = open(os.path.join(log_dir, "bug_server" + str(time.time())[:10] + ".txt"), "w+")
std_file = open(os.path.join(log_dir, "std_server" + str(time.time())[:10] + ".txt"), "w+")
print(cmd_str)
pid = subprocess.Popen(cmd_str.split(), stdout=std_file, stderr=bug_file, shell=False)
print(pid.pid)











