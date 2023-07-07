# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import sys

sys.path.append(r"/usr/code/test")

import os
import subprocess
import time


rtmp_url = "rtmp://58.240.116.75:51935/swp/TX00100004?secret=0353f7-6b-4889-a715-eb2d1925cc"
output_file = r"./del.pcm"


if(os.path.exists(output_file)):
    os.remove(output_file)

log_file_handle = open(r"./rtmp.log", "w")
# 启动子进程，并重定向输出
process = subprocess.Popen(
    ["ffmpeg", "-i", rtmp_url, "-f", "s16le", "-acodec", "pcm_s16le", "-ac", "1", "-ar", "16000", output_file],
    stdout=log_file_handle,
    stderr=log_file_handle
)

time.sleep(8)

log_file_xunfei = open(r"./xunfei.log", "w")
process_2 = subprocess.Popen(
    ["./awaken_offline_sample",  "./del.pcm",   "http://example.com"],
    stdout=log_file_xunfei,
    stderr=log_file_xunfei
)


time.sleep(60)

print(process.pid)
process.terminate()

print(process_2.pid)
process_2.terminate()
