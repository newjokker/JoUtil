# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import socket
import time
import cv2
import uuid

# fixme 使用 UDP 发送的太快，来不及接受，很多图片都是不完整的，所以传输视频图像还是使用 TCP 比较好
# fixme UDP 想发送完整的图片的话需要每次发送之后等待一下再去发送
# UDP 在发送小文件并且不太在意丢失数据的时候比较实用

# ----------------------------------------------------------------------------------------------------------------------
HOST = "192.168.3.221"
PORT = 12121
buff_size = 50000
rtsp = r"rtsp://admin:txkj-2021@192.168.3.17:554/Streaming/Channels/501"
# ----------------------------------------------------------------------------------------------------------------------

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
start_time = time.time()
sock = socket.socket()

# if buff_size
recv_buff = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
send_buff = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
if buff_size > send_buff:
    raise ValueError(" buff_size need less then send_buff - 100")

index = 0
cap = cv2.VideoCapture(rtsp)

while True:
    server_address = (HOST, PORT)
    ret, frame = cap.read()
    if ret:
        index += 1
        success, encoded_image = cv2.imencode(".jpg", frame)
        if success:
            byte_data = encoded_image.tobytes()
            uuid_index = str(uuid.uuid1())
            for i in range(0, len(byte_data), buff_size):
                client_socket.sendto(bytes(uuid_index.encode('utf-8')) + byte_data[i:i+buff_size], server_address)


