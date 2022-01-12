# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import dlib
import cv2
import cv2
import dlib
import matplotlib.pyplot as plt
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil
import os

# refer : https://blog.csdn.net/Roaddd/article/details/111866756

# 使用 Dlib 的正面人脸检测器 frontal_face_detector
#
# # 图片所在路径
# img = cv2.imread(r'C:\Users\14271\Desktop\del\face.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# # 人脸检测
# detector = dlib.get_frontal_face_detector()
# dets = detector(img, 1)
# # 关键点检测
# # 模型的下载路径：http://dlib.net/files/
# predictor = dlib.shape_predictor(r'C:\Users\14271\Desktop\del\shape_predictor_68_face_landmarks.dat')
#
# for det in dets:
#     shape = predictor(img, det)
#     print(shape.parts())
#
#     # 人脸对齐
#     my_img = dlib.get_face_chip(img, shape, size=150)
#
#     plt.imshow(my_img)
#     plt.show()
#

img_dir = r"C:\Users\14271\Desktop\res"
save_dir = r"C:\Users\14271\Desktop\human_xml"

detector = dlib.get_frontal_face_detector()
for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg', '.JPG', '.png', '.PNG']):
    print(each_img_path)
    each_dete_res = DeteRes(assign_img_path=each_img_path)
    img = cv2.imread(each_img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    dets = detector(img, 1)
    for each_shape in dets:
        each_dete_res.add_obj(x1=int(each_shape.left()), y1=int(each_shape.top()), x2=int(each_shape.right()), y2=int(each_shape.bottom()), tag='face')
    each_dete_res.save_to_xml(os.path.join(save_dir, FileOperationUtil.bang_path(each_img_path)[1] + '.xml'))


