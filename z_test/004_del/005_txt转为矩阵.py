# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import numpy as np
import matplotlib.pyplot as plt


# 读取 txt 中的 矩阵，长宽为固定的 150 * 150

txt_server_path = r"C:\data\005_中山项目\002_对比预处理之间的差异\aaa_zhongshan\DJI_0032\DJI_0032_server.txt"
npy_path = r"C:\data\005_中山项目\002_对比预处理之间的差异\aaa_zhongshan\DJI_0032\DJI_0032.npy"
txt_path = r"C:\data\005_中山项目\002_对比预处理之间的差异\aaa_zhongshan\DJI_0032\DJI_0032.txt"

# img_server = np.load(npy_path)
img = np.load(npy_path)

img_server = np.loadtxt(txt_server_path)

img_server.resize([3,150,150])

print(np.mean(img_server))

# with open(txt_path, 'r') as txt_file:
#     mat_str = txt_file.readline()
#     mat = mat_str.strip().split(" ")
#     mat = list(map(float, mat))
#     img = np.array(mat)
#
#     # img = img * 255.0
#
#     img.resize([3,150,150])
#
#     # img.flatten()
#
#     # print(img.shape)
#     # img = img.astype(np.uint8)
#     # plt.imshow(img[0, 1,:,:])
#     # plt.show()
#
#     print(img.shape)


# a = img_server - img
# #
# # print(np.mean(img))
# #
# # print(np.sum(a))
# #
# a = np.abs(a) * 100
# a = a.astype(np.uint8)
#
#
# plt.imshow(a[1,:,:])
# plt.show()

#
img_server = img_server * 255
img_server = img_server.astype(np.uint8)
#
plt.imshow(img_server[1,:,:], cmap='gray')
plt.show()






print("OK")

