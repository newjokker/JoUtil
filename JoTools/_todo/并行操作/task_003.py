# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# refer : https://blog.csdn.net/weixin_43283397/article/details/104294890


# 跑的时候必须在  __name__ == "__main__" 下面跑
# 貌似比 task002 要快一些，不知道原因
# 要先 close 再去 join(阻塞)


from multiprocessing import Pool
from JoTools.utils.FileOperationUtil import FileOperationUtil
import cv2
import time



def print_img_shape(img_path, times=5):
    for _ in range(times):
        img = cv2.imread(img_path)
        print(img.shape)


if __name__ == "__main__":


    start_time = time.time()
    img_dir = r"C:\Users\14271\Desktop\del\pillow_cv2"
    image_list = list(FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg']))

    pool = Pool(4)

    for each_img_path in image_list:
        pool.apply_async(print_img_shape, (each_img_path, 5, ))

    pool.close()
    pool.join()

    end_time = time.time()
    print("use time : {0} s".format(end_time - start_time))




























