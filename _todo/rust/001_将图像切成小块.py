# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import numpy as np
from PIL import Image
import random
import os
import cv2
import matplotlib.pyplot as plt


class SegmentAndRegroup(object):
    """对图片进行切块并重组，两种模式（1）设定横竖格分为几块（2）设定每个 block 的长宽"""

    def __init__(self):
        self.segment_x = 7  # 沿着 x 轴 切分的块数
        self.segment_y = 7
        self.img_path = None
        self.img_array = None
        self.img_array_origin = None  # 原始图片矩阵，因为要使得每一个分块一样大，所以需要去掉边缘的像素
        self.exchange_times = None # 区块之间两两交换的次数
        self.assign_block_height = None  # 指定 block 的长度
        self.assign_block_width = None
        self.assign_block_size = False  # 使用指定大小的 block 进行分类
        self.save_dir = None

    def get_segment_x_y(self):
        """获得横纵向裁剪的个数"""
        if self.assign_block_size:
            # 当指定使用固定大小的 block 的时候
            if self.assign_block_width is None or self.assign_block_height is None:
                raise ValueError("需要指定 block 的长宽")
            #
            self.segment_x = int(self.img_array_origin.shape[1] / self.assign_block_width)
            self.segment_y = int(self.img_array_origin.shape[0] / self.assign_block_height)

    def get_array_from_img(self):
        """将图片的转为 array"""
        # fixme 现在默认为的是输入有 rgb三通道的 .jpg 图片
        img = Image.open(self.img_path)
        img_array = np.array(np.asarray(img, dtype=np.uint8))
        img_array.flags.writeable = True  # 解决图片为 read only 的问题
        # 如果 img_array 是只有一个通道扩展为 3 通道
        if len(img_array.shape) == 2:
            img_array = np.rollaxis(np.tile(img_array, (3, 1, 1)), 0, 3)

        height, width, = img_array.shape[:2]
        self.img_array_origin = img_array
        # 根据设置的分块模式设定横竖切块个数
        self.get_segment_x_y()
        # 将不能分块的边缘先去掉
        self.img_array = img_array[:height-(height % self.segment_y), :width-(width % self.segment_y), :]
        # 当没指定 block size 时，计算得到 block size
        if not self.assign_block_size:
            self.assign_block_width = int(self.img_array.shape[1] / self.segment_x)
            self.assign_block_height = int(self.img_array.shape[0] / self.segment_y)

    def save_array_to_img(self, save_path):
        """将 array 转为图片"""
        height, width = self.img_array.shape[:2]
        self.img_array_origin[:height, :width, :] = self.img_array
        img = Image.fromarray(self.img_array_origin)
        img.save(save_path)

    def change_random_block(self):
        """随机交换两个 block，block 的位置是随机的"""
        height, width, _ = self.img_array.shape
        x1 = random.randint(0, int((height - self.assign_block_height)/50))
        x2 = random.randint(0, int((height - self.assign_block_height)/50))
        y1 = random.randint(0, int((width - self.assign_block_width)/50))
        y2 = random.randint(0, int((width - self.assign_block_width)/50))

        x1,x2,y1,y2 = x1*50, x2*50, y1*50, y2*50

        block_1 = self.img_array[x1:x1+50, y1:y1+50, :]
        self.img_array[x1:x1 + 50, y1:y1 + 50, :] = self.img_array[x2:x2+50, y2:y2+50, :]
        self.img_array[x2:x2+50, y2:y2+50, :] = block_1

    def get_mat_in_assign_block(self, block_xy):
        """获取指定区块的矩阵"""
        x_min_1, y_min_1 = self.assign_block_width * block_xy[1], self.assign_block_height * block_xy[0]
        x_max_1, y_max_1 = x_min_1 + self.assign_block_width, y_min_1 + self.assign_block_height
        return self.img_array[y_min_1:y_max_1, x_min_1:x_max_1, :]

    def do_process(self, save_path):
        """主流程"""
        # 从图像获取矩阵，对分割 block 数目和 block 大小进行确定
        if self.get_array_from_img() is False:
            print("目前只能处理 rgb 图")
            return

        for i in range(100):
            self.change_random_block()

        # # 根据需要打乱的次数打乱区块
        # for i in range(self.segment_x):
        #     for j in range(self.segment_y):
        #         print(i, j)
        #         each_mat = self.get_mat_in_assign_block((j, i))
        #         img = Image.fromarray(each_mat)
        #         each_save_path = os.path.join(self.save_dir, "{0}_{1}.jpg".format(i, j))
        #         img.save(each_save_path)

        self.save_array_to_img(save_path)

def segment_and_regroup(img_path, save_path, exchange_times=10, segment_x=7, segment_y=7, assign_block_size=False,
                        assign_block_width=None, assign_block_heignt=None):
    a = SegmentAndRegroup()
    a.save_dir = r"C:\Users\14271\Desktop\del\crop"
    a.img_path = img_path
    a.segment_x = segment_x
    a.segment_y = segment_y
    a.exchange_times = exchange_times
    # 当使用指定 block 大小的时候，指定的切割长宽个数参数将重新计算
    a.assign_block_size = assign_block_size
    a.assign_block_height = assign_block_heignt
    a.assign_block_width = assign_block_width
    a.do_process(save_path)

# ----------------------------------------------------------------------------------------------------------------------


# H表示色彩/色度，取值范围 [0，179]，S表示饱和度，取值范围 [0，255]，V表示亮度，取值范围 [0，255]

# frame = cv2.imread(r"C:\Users\14271\Desktop\del\ok.jpg")
# hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# h, s, v = hsv[:,:,0], hsv[:,:,1], hsv[:,:,2]
#
# # plt.figure()
# # plt.imshow(h, cmap='gray')
# # plt.figure()
# # plt.imshow(v, cmap='gray')
#
# # todo 画出颜色直方图
# hist = cv2.calcHist([hsv], [0], None, [50], [0,256])
#
# plt.plot(hist)
#
# plt.show()





if __name__ == "__main__":

    JpgPath = r"C:\Users\14271\Desktop\del\rust.jpg"
    SavePath = r"C:\Users\14271\Desktop\del\rust_2.jpg"
    # segment_and_regroup(JpgPath, SavePath, 10, assign_block_size=True, assign_block_heignt=100, assign_block_width=100)
    segment_and_regroup(JpgPath, SavePath, 20, assign_block_heignt=80, assign_block_width=80, assign_block_size=True)
