# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import argparse
import cv2
from .fzc_broken_rust import FzcBrokenRust

fzc = FzcBrokenRust()


model_list = [fzc]

def get_ndarry_from_img(img_path):
    return 123


def parse_args():
    parser = argparse.ArgumentParser(description='Tensorflow Faster R-CNN demo')
    #
    parser.add_argument('--imgDir',dest='imgDir',type=str, default=r"/usr/input_picture")
    parser.add_argument('--modelList',dest='modelList',default="M1,M2,M3,M4,M5,M6,M7,M8,M9")
    parser.add_argument('--jsonPath',dest='jsonPath', default=r"/usr/input_picture_attach/pictureName.json")
    parser.add_argument('--outputDir',dest='outputDir', default=r"/usr/output_dir")
    #
    parser.add_argument('--scriptIndex',dest='scriptIndex', default=r"1-1")
    #
    parser.add_argument('--gpuID', dest='gpuID',type=int,default=0)
    parser.add_argument('--port',dest='port',type=int,default=45452)
    parser.add_argument('--gpuRatio',dest='gpuRatio',type=float,default=0.3)
    parser.add_argument('--host',dest='host',type=str,default='127.0.0.1')
    parser.add_argument('--logID',dest='logID',type=str,default=str(uuid.uuid1())[:6])
    parser.add_argument('--objName',dest='objName',type=str,default='')
    #
    args = parser.parse_args()
    return args





if __name__ == "__main__":

    args = parse_args()

    # model restore
    for each in model_list:
        each.model_restore(args)

    # detect
    for each_img_path in img_list:
        each_img_ndarry = get_ndarry_from_img(each_img_path)
        for each in model_list:
            each.model_detect(each_img_ndarry)








