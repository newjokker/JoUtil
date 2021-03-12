# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import cv2
import os
import random
import copy
import numpy as np
import uuid
from JoTools.utils.FileOperationUtil import FileOperationUtil

# 边缘区域无法是一个 block 的就先不管了


def mix_blocks_in_img(img_path, save_path, block_width=30):
    """混淆图片中的各个 blocks"""
    img_mat = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)
    height, width, _ = img_mat.shape
    #
    block_width = int(max(width, height) / 10)
    block_x_index = int(width/block_width)
    block_y_index = int(height/block_width)

    for i in range(block_x_index*block_y_index):
        x1, x2 = random.randint(0, block_y_index-1), random.randint(0, block_y_index-1)
        y1, y2 = random.randint(0, block_x_index-1), random.randint(0, block_x_index-1)

        temp_block_a = copy.deepcopy(img_mat[x1* block_width:(x1+1)* block_width, y1* block_width:(y1+1)* block_width, :])
        temp_block_b = copy.deepcopy(img_mat[x2* block_width:(x2+1)* block_width, y2* block_width:(y2+1)* block_width, :])

        img_mat[x1*block_width:(x1+1)*block_width, y1*block_width:(y1+1)*block_width, :] = temp_block_b
        img_mat[x2*block_width:(x2+1)*block_width, y2*block_width:(y2+1)*block_width, :] = temp_block_a

    cv2.imencode('.jpg', img_mat)[1].tofile(save_path)



if __name__ == "__main__":

    img_dir = r"C:\Users\14271\Desktop\金具锈蚀完善\ljcRust测试集\crop"

    for index, each_img_path in enumerate(FileOperationUtil.re_all_file(img_dir, lambda x:str(x).endswith(".jpg"))):
        print(index, each_img_path)
        mix_blocks_in_img(each_img_path, each_img_path)








