# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import time
from socket import socket, AF_INET, SOCK_STREAM


s = socket(AF_INET, SOCK_STREAM)
s.connect(('192.168.3.221', 12211))


for i in range(1000):

    s.send(b'length_0000'.ljust(1024, b'0'))
    # print(s.recv(2))
    time.sleep(0.5)


# print(s.recv(8192))

