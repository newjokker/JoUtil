# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import time
import shutil
import random
import argparse
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.HashlibUtil import HashLibUtil

# 读取图片，处理图片，得到结果

def parse_args():
    parser = argparse.ArgumentParser(description='Tensorflow Faster R-CNN demo')
    parser.add_argument('--imgDir',dest='img_dir',type=str, default=r"C:\Users\14271\Desktop\del\input_dir")
    parser.add_argument('--modelList',dest='model_list',default="M1,M2,M3,M4,M5,M6,M7,M8,M9")
    parser.add_argument('--jsonPath',dest='json_path', default=r"/usr/input_picture_attach/pictureName.json")
    parser.add_argument('--outputDir',dest='output_dir', default=r"/usr/output_dir")
    parser.add_argument('--scriptIndex',dest='script_index', default=r"1-1")
    parser.add_argument('--gpuID', dest='gpuID',type=int,default=0)
    args = parser.parse_args()
    return args

def lock_img_path(img_path):
    """对文件名进行加锁"""
    if img_path.endswith('.lock'):
        raise TypeError("already locked")
    else:
        img_path_locked = img_path + '.lock'
        shutil.move(img_path, img_path_locked)
        return img_path_locked

def unlock_img_path(img_path):
    """文件解锁"""
    if not img_path.endswith('.lock'):
        raise TypeError("not locked")
    else:
        img_path_unlocked = img_path[:-5]
        shutil.move(img_path, img_path_unlocked)
        return img_path_unlocked

def is_locked(img_path):
    """判断文件是否被锁"""
    if img_path.endswith('.lock'):
        return True
    else:
        return False

def deal_with_img(img_path):
    """图片处理"""
    md5_str = HashLibUtil.get_file_md5(img_path)
    # time.sleep(1)
    return md5_str


if __name__ == "__main__":

    args = parse_args()

    img_dir = args.img_dir

    # for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg', '.JPG', '.png', '.PNG']):
    index = 1

    img_path_list = list(FileOperationUtil.re_all_file(img_dir))
    random.shuffle(img_path_list)

    for each_img_path in img_path_list:
        #
        try:
            if is_locked(each_img_path):
                continue
            #
            if os.path.exists(each_img_path):
                locked_img_path = lock_img_path(each_img_path)
            else:
                continue
            #
            md5_str = deal_with_img(locked_img_path)
            #
            if os.path.exists(locked_img_path):
                os.remove(locked_img_path)
                # unlock_img_path(locked_img_path)
            else:
                continue

            print(index, md5_str)
            index += 1

        except FileNotFoundError:
            print("-no file-")

        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])
            print(e.__traceback__.tb_lineno)



























