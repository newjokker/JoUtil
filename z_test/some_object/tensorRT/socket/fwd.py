# -*- coding: utf-8  -*-
# -*- author: jokker -*-

###服务器端server.py
import socket
import os
import sys
import struct
import uuid
import cv2
import numpy as np


def socket_service_image():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # s.bind(('127.0.0.1', 6666))
        s.bind(('0.0.0.0', 1122))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)

    print("Wait for Connection.....................")

    while True:
        sock, addr = s.accept()  # addr是一个元组(ip,port)
        deal_image(sock, addr)


def deal_image(sock, addr):
    print("Accept connection from {0}".format(addr))  # 查看发送端的ip和端口

    while True:
        fileinfo_size = struct.calcsize('128sq')
        buf = sock.recv(fileinfo_size)
        if buf:
            filename, filesize = struct.unpack('128sq', buf)
            fn = filename.decode().strip('\x00')
            new_filename = os.path.join('./res/', 'new_{0}'.format(str(uuid.uuid1())) + fn)

            recvd_size = 0
            res = b""

            while not recvd_size == filesize:
                if filesize - recvd_size > 1024:
                    data = sock.recv(1024)
                    recvd_size += len(data)
                    res += data
                else:
                    data = sock.recv(1024)
                    recvd_size = filesize
                    res += data

            print(len(res))
            img_np_arr = np.fromstring(res, np.uint8)
            im = cv2.imdecode(img_np_arr, cv2.COLOR_BGR2RGB)

        sock.close()
        break


if __name__ == '__main__':
    index = 0

    a = ['1', '2', '3']

    socket_service_image()





