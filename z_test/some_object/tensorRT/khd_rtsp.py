# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import socket
import os
import sys
import struct
import time
import cv2
import argparse

sign_dir = r"/home/tensorRT/tensorrt_test/logs/sign"


def dete_error():
    """检测失败，发出失败的信号"""
    sign_txt = os.path.join(sign_dir, 'restart.txt')
    with open(sign_txt, 'w') as sign_file:
        sign_file.write("error")


def sock_client_image(args):

    index = 1
    start_time = time.time()
    cap = cv2.VideoCapture(args.rtsp)

    save_img_dir = r"/home/tensorRT/tensorrt_test/rtsp_img"
    os.makedirs(save_img_dir, exist_ok=True)
    print("* push start : {0}".format(start_time))

    while True:

        try:

            ret, frame = cap.read()
            if ret:
                index += 1
                if index % 100 == 0:
                    save_path = os.path.join(save_img_dir, "{0}.jpg".format(index))
                    cv2.imwrite(save_path, frame)

                success, encoded_image = cv2.imencode(".jpg", frame)
                if success:
                    byte_data = encoded_image.tobytes()
                else:
                    continue
                #
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((args.host, args.port))
                fhead = struct.pack(b'128sq', bytes("filepath", encoding='utf-8'), len(byte_data))
                s.send(fhead)
                s.send(byte_data)
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])
            print(e.__traceback__.tb_lineno)
            print("* restart server")
            dete_error()
            time.sleep(10)


def parse_args():
    parser = argparse.ArgumentParser(description='Tensorflow Faster R-CNN demo')
    parser.add_argument('--port', dest='port', type=int, default=222)
    parser.add_argument('--host', dest='host', type=str, default='192.168.3.132')
    parser.add_argument('--rtsp', dest='rtsp', type=str, default=r"rtsp://admin:txkj123!@192.168.3.19:554/Streaming/Channels/101")
    args = parser.parse_args()
    return args



if __name__ == '__main__':

    args = parse_args()
    sock_client_image(args)

