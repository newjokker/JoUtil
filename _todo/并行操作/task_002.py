# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from JoTools.utils.FileOperationUtil import FileOperationUtil
import cv2
import time


def print_img_shape(img_path):
    for _ in range(5):
        img = cv2.imread(img_path)
        print(img.shape)


start_time = time.time()
img_dir = r"C:\Users\14271\Desktop\del\pillow_cv2"

image_list = FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg'])

# ----------------------------------------------------------------------------------------------------------------------
pool = ThreadPool(4)                            # Sets the pool size to 4
pool.map(print_img_shape, image_list)
pool.close()                                    # 进程池close的时候并未关闭进程池，使其不再接受新的（主进程）任务
pool.join()                                     # 主进程阻塞后，让子进程继续运行完成，子进程运行完后，再把主进程全部关掉
# ----------------------------------------------------------------------------------------------------------------------

# 使用非多进程
# for each_img_path in image_list:
#     print_img_shape(each_img_path)

# ----------------------------------------------------------------------------------------------------------------------

end_time = time.time()
print("use time : {0} s".format(end_time - start_time))


"""
# 线程数与消耗的时间

pool_size,time

0,13.48
1,13.57
2,7.79
3,5.41
4,4.37
5,3.74
6,3.44
7,3.47
8,3.42
9,3.39

# 结论是对于读取图片任务，使用多进程是能较大提升脚本的效率的

"""


























