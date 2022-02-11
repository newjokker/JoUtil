# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import cv2
import time


video_source = "rtsp://admin:txkj-2021@192.168.3.17:554/Streaming/Channels/401"

cap = cv2.VideoCapture(video_source)

while True:
    ret, frame = cap.read()

    print(ret)
    print(frame)
    print('-'*50)







