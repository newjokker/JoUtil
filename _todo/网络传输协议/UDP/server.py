# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import socket
import time
import cv2
import numpy as np
import uuid
import os

# ----------------------------------------------------------------------------------------------------------------------
PORT = 12121
HOST= "0.0.0.0"
uuid_size = 36
buff_size = 60000
# ----------------------------------------------------------------------------------------------------------------------

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))
server_socket.settimeout(60*60*24)

front_index = '0'*uuid_size
img_data = b""
index = 0
start_time = time.time()

def func_depend_frame(frame, index):
    print(frame.shape)
    # cv2.imwrite(os.path.join(r"/home/ldq/UDP/img", "{0}.jpg".format(index)), frame)


if __name__ == "__main__":


    while True:
        now = time.time()
        # refer : https://blog.csdn.net/whatday/article/details/89964168
        receive_data, client = server_socket.recvfrom(buff_size)
        uuid_index, each_img_data = receive_data[:uuid_size], receive_data[uuid_size:]
        #
        if (uuid_index != front_index) and img_data:
            #
            print(len(img_data))
            img_np_arr = np.fromstring(img_data, np.uint8)
            frame = cv2.imdecode(img_np_arr, cv2.COLOR_BGR2RGB)
            #
            if isinstance(frame, np.ndarray):
                index += 1
                func_depend_frame(frame, index)
            #
            img_data = each_img_data
            front_index = uuid_index
        else:
            img_data += each_img_data


