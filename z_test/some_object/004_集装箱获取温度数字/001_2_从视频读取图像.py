# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import cv2
vc = cv2.VideoCapture(r'C:\Users\14271\Desktop\sifang\test_001\H121201-1_20210222140550_20210222145435.dav')
c=0
rval=vc.isOpened()

while rval:
    c = c + 1
    rval, frame = vc.read()
    if rval:
        cv2.imwrite(r'C:\Users\14271\Desktop\vedio_img'+'camera1_binggan'+str(c) + '.jpg', frame) #命名方式
        print(c)
    else:
        break
vc.release()
