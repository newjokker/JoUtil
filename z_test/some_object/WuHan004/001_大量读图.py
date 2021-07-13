# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import cv2
import numpy as np
from JoTools.for_csdn.word_pic.word_pic import WordImage
from PIL import Image
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.DecoratorUtil import DecoratorUtil
import concurrent.futures
import glob

@DecoratorUtil.time_this
def read_img(img_path):

    # img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_0_标准测试集\img"
    # index = 0
    # for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg']):
    #     index += 1
    img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)
    print(index, img.shape)



if __name__ == "__main__":

    with concurrent.futures.ProcessPoolExecutor() as executor:  ## 默认为1
        img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_0_标准测试集\img"
        # image_files = list(FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg']))
        image_files = glob.glob(img_dir + '\\*.jpg')
        executor.map(read_img, image_files)
