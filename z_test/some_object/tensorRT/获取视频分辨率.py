# -*- coding: utf-8  -*-
# -*- author: jokker -*-
import cv2




rtsp = r"rtsp://admin:admin123@192.168.3.52:554/Streaming/Channels/101"



try:
    # 孾^彗¶罎·住~V覾F顾Q轕¿宽潚~D大対O﻾L仼 纾Y彜~M佊¡端
    import cv2
    cap = cv2.VideoCapture(rtsp)
    w, h = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    ret, frame = cap.read()

    if ret:
        print(ret.shape)


except Exception as e:
    print('-'*50)
    print(e)
    print('-'*50)


print(h)
print(w)





