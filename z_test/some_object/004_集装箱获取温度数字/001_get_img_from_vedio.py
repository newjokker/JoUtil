# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import cv2
from JoTools.utils.VideoUtilCV import VideoUtilCV



# vedio_path = r"D:\AppData\baiduwangpan\视频识别\H121202-2_20210222114626_20210222120540.dav"
vedio_path = r"D:\AppData\baiduwangpan\视频识别\H121202-2_20210222114626_20210222120540.dav"
save_dir = r"C:\Users\14271\Desktop\del\crop_vedio"



vc = cv2.VideoCapture(vedio_path)
c=0
rval=vc.isOpened()

sep = 120
while rval:
    c = c + 1
    for i in range(sep):
        rval, frame = vc.read()

    if rval:
        cv2.imwrite(os.path.join(save_dir, str(c)+'.jpg'),  frame) #命名方式
    else:
        break
vc.release()










# VideoUtilCV.get_img_from_vedio(vedio_path, save_dir, sep=600)


