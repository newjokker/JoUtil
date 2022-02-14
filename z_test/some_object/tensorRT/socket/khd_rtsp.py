# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import socket
import os
import sys
import struct
import time
import cv2
import argparse


def sock_client_image(args):

    index = 0
    start_time = time.time()
    cap = cv2.VideoCapture(args.rtsp)

    while True:
        print(index / (time.time() - start_time))
        #
        ret, frame = cap.read()
        if ret:
            index += 1
            success, encoded_image = cv2.imencode(".jpg", frame)
            if success:
                byte_data = encoded_image.tobytes()
            else:
                continue
            #
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((args.host, args.port))
                fhead = struct.pack(b'128sq', bytes("filepath", encoding='utf-8'), len(byte_data))
                s.send(fhead)
                s.send(byte_data)
            except socket.error as msg:
                print(msg)
                time.sleep(3)
                exit()

def parse_args():
    parser = argparse.ArgumentParser(description='Tensorflow Faster R-CNN demo')
    parser.add_argument('--port', dest='port', type=int, default=1211)
    parser.add_argument('--host', dest='host', type=str, default='192.168.3.221')
    parser.add_argument('--rtsp', dest='rtsp', type=str, default=r"rtsp://admin:txkj-2021@192.168.3.17:554/Streaming/Channels/501")
    args = parser.parse_args()
    return args



if __name__ == '__main__':

    args = parse_args()
    sock_client_image(args)

