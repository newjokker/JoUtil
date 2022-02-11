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

def sock_client_image():

    filepath = r"C:\Users\14271\Desktop\del\face.jpg"

    start_time = time.time()

    index = 0

    while True:

        if time.time() - start_time > 0.05:
            break

        index += 1
        print(index)

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('192.168.3.221', 1122))  # 服务器和客户端在不同的系统或不同的主机下时使用的ip和端口，首先要查看服务器所在的系统网卡的ip
        except socket.error as msg:
            print(msg)
            print(sys.exit(1))

        # filepath = input('input the file: ')  # 输入当前目录下的图片名 xxx.jpg
        fhead = struct.pack(b'128sq', bytes(os.path.basename(filepath), encoding='utf-8'), os.stat(filepath).st_size)  # 将xxx.jpg以128sq的格式打包
        s.send(fhead)

        fp = open(filepath, 'rb')  # 打开要传输的图片
        while True:
            data = fp.read()  # 读入图片数据
            if not data:
                print('{0} send over...'.format(filepath))
                break
            s.send(data)  # 以二进制格式发送图片数据
        s.close()


if __name__ == '__main__':
    sock_client_image()

