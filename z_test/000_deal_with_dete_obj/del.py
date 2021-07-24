# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import cv2
import JoTools.txkjRes as txkj
from skimage.measure import find_contours
import matplotlib.pyplot as plt
import numpy as np


# 根据 mask 拿到轮廓

img = cv2.imread(r"C:\Users\14271\Desktop\test\test.png")

print(img.shape)

img = img[:,:,1]

# print(img.shape)
#
# a = find_contours(img[:,:,1], 1, fully_connected='low')
#
# print(len(a))
#
# for points in a:
#     print(len(points))
#
#     # x, y = zip(*points)
#     # x = list(map(lambda x:int(x), x))
#     # y = list(map(lambda x:int(x), y))
#
#     for point in points:
#         point = tuple([int(point[1]), int(point[0])])
#         cv2.circle(img, point, 5, [1,255,1], 1)
#
#     # cv2.circle(img, (x,y), 5, [1,255,1], 1)
#
# plt.imshow(img)
# plt.show()





# import numpy as np
# import matplotlib.pyplot as plt
# from skimage import measure,draw

# #生成二值测试图像
# img=np.zeros([100,100])
# img[20:40,60:80]=1  #矩形
# rr,cc=draw.circle(60,60,10)  #小圆
# rr1,cc1=draw.circle(20,30,15) #大圆
# img[rr,cc]=1
# img[rr1,cc1]=1



# ----------------------------------------------------------------------------------------------------------------------

#检测所有图形的轮廓
contours = find_contours(img, 0.5)


# contours = np.delete(contours[0], list(range(500)),axis=1)

#绘制轮廓
fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(2,2))
ax0.imshow(img,plt.cm.gray)
ax1.imshow(img,plt.cm.gray)
for n, contour in enumerate(contours):
    # 删除其中的几行，确保每个形状只保留不到 60 个关键点
    del_list = [i for i in range(1, len(contour)-1) if i % int(len(contour)/60) != 0]
    contour = np.delete(contour, del_list, axis=0)
    print(len(contour))
    #
    ax1.plot(contour[:, 1], contour[:, 0], linewidth=2)
ax1.axis('image')
ax1.set_xticks([])
ax1.set_yticks([])
plt.show()


# ----------------------------------------------------------------------------------------------------------------------


# import cv2
#
# img = cv2.imread(r"C:\Users\14271\Desktop\del\112233.png")
# img = img[:,:,1]
#
# binary = img > 20
#
# # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
#
# contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
#
# cv2.imshow("img", img)
# cv2.waitKey(0)
#


