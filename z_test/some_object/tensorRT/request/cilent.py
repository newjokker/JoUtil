# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import cv2
import time
import requests

# 不断解析 rtsp 流的图片，传给服务端


# video_source = "rtsp://192.168.3.132:5454/test.264"
# video_source = "rtsp://admin:txkj-2021@192.168.3.17:554/Streaming/Channels/401"
video_source = "rtsp://admin:txkj-2021@192.168.3.17:554/Streaming/Channels/501"
print(video_source)

url = r"http://192.168.3.221:1211/test"
# url = r"http://192.168.3.185:1211/test"


# todo 在这边根据返回的 stack 的长度来控制是否进行推送，这样来控制能实时检测

top = 200

cap = cv2.VideoCapture(video_source)

start_time = time.time()
index = 0

while True:

    if time.time() - start_time > 500:
        break

    ret, frame = cap.read()
    if ret:
        #
        success, encoded_image = cv2.imencode(".jpg", frame)
        byte_data = encoded_image.tobytes()
        files = {'image': byte_data}
        res = requests.post(url=url, files=files)

        index += 1
        print(index, frame.shape)


