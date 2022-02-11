# -*- coding: utf-8  -*-
# -*- author: jokker -*-

'''
Fuction：客户端发送图片和数据
Date：2018.9.8
Author：snowking
'''
###客户端client.py
import socket
import os
import sys
import struct
import time
import cv2


def sock_client_image():

    filepath = r"C:\Users\14271\Desktop\del\face_3.jpg"

    start_time = time.time()

    index = 0

    cap = cv2.VideoCapture(r"rtsp://admin:txkj-2021@192.168.3.17:554/Streaming/Channels/501")

    while True:

        if time.time() - start_time > 200000:
            break

        ret, frame = cap.read()
        # ret, frame = cap.read()
        # ret, frame = cap.read()

        if ret:
            #
            success, encoded_image = cv2.imencode(".jpg", frame)
            byte_data = encoded_image.tobytes()
        else:
            continue

        index += 1
        # print(index)

        print(index/(time.time()-start_time))

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('192.168.3.221', 1211))  # 服务器和客户端在不同的系统或不同的主机下时使用的ip和端口，首先要查看服务器所在的系统网卡的ip
            fhead = struct.pack(b'128sq', bytes(os.path.basename(filepath), encoding='utf-8'), len(byte_data))  # 将xxx.jpg以128sq的格式打包
            s.send(fhead)
            s.send(byte_data)  # 以二进制格式发送图片数据
            # s.close()
        except socket.error as msg:
            print(msg)
            print(sys.exit(1))


if __name__ == '__main__':
    sock_client_image()

