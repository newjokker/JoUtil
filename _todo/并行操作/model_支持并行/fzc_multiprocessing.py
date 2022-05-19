# -*- coding: UTF-8 -*-
# !/usr/bin/env python

# --------------------------------------------------------
# Tensorflow Faster R-CNN
# Licensed under The MIT License [see LICENSE for details]
# Written by Xinlei Chen, based on code from Ross Girshick
# --------------------------------------------------------

import os, sys

this_dir = os.path.dirname(__file__)
lib_path = os.path.join(this_dir, '..')
sys.path.insert(0, lib_path)
import argparse
import cv2
import json
import torch
import numpy as np
import threading
from PIL import Image
import uuid
import time

from lib.detect_libs.yolov5Detection import YOLOV5Detection
from lib.detect_utils.timer import Timer
from lib.detect_libs.fasterDetectionPyTorch import FasterDetectionPytorch
from lib.detect_libs.vggClassify import VggClassify
from lib.detect_libs.clsDetectionPyTorch import ClsDetectionPyTorch
from lib.detect_libs.ljcY5Detection import LjcDetection
from lib.detect_libs.kkgY5Detection import KkgDetection
from lib.detect_libs.clsDetectionPyTorch import ClsDetectionPyTorch
from lib_xjQX.detect_libs.ljjxjR2cnnDetection import ljcR2cnnDetection
from lib_xjQX.detect_libs.xjDeeplabDetection import xjDeeplabDetection
#
from lib.JoTools.txkjRes.resTools import ResTools
from lib.JoTools.utils.FileOperationUtil import FileOperationUtil
from lib.JoTools.utils.CsvUtil import CsvUtil
from lib.JoTools.txkjRes.deteRes import DeteRes
from lib.JoTools.txkjRes.deteObj import DeteObj
from lib.JoTools.txkjRes.deteAngleObj import DeteAngleObj
from lib.JoTools.utils.JsonUtil import JsonUtil

# vit
from lib.detect_libs.clsViTDetection import ClsViTDetection

# ThreadPool
from multiprocessing.dummy import Pool as ThreadPool


def detect_fzc(img_path):
    """fzc 检测"""

    data = {'path': img_path}

    name = 'test'

    dete_res_all = DeteRes()
    dete_res_all.imgPath = img_path

    try:
        # step_1
        dete_res_fzc = model_fzc_1.detectSOUT(path=data['path'], image_name=name)
        # step_2
        for each_dete_obj in dete_res_fzc:
            crop_array = dete_res_fzc.get_sub_img_by_dete_obj(each_dete_obj, RGB=False,
                                                              augment_parameter=[0.1, 0.1, 0.1, 0.1])
            new_label, conf = model_fzc_2.detect_new(crop_array, name)
            #
            each_dete_obj.tag = new_label
            each_dete_obj.conf = conf

            #
            if each_dete_obj.tag == "fzc_broken":
                if each_dete_obj.conf > 0.9:
                    each_dete_obj.tag = "fzc_broken"
                else:
                    each_dete_obj.tag = "other_fzc_broken"
            elif each_dete_obj.tag == "other":
                each_dete_obj.tag = "other_other"
            else:
                if each_dete_obj.conf > 0.6:
                    each_dete_obj.tag = "Fnormal"
                else:
                    each_dete_obj.tag = "other_Fnormal"
            #
            dete_res_all.add_obj_2(each_dete_obj)
            dete_res_all.save_to_xml(os.path.join(save_dir, os.path.split(img_path)[1][:-4] + '.xml'))

    except Exception as e:
        print(e)
        print(e.__traceback__.tb_frame.f_globals["__file__"])
        print(e.__traceback__.tb_lineno)


def parse_args():
    parser = argparse.ArgumentParser(description='Tensorflow Faster R-CNN demo')
    #
    parser.add_argument('--imgDir', dest='imgDir', type=str, default=r"/usr/input_picture")
    parser.add_argument('--modelList', dest='modelList', default="M1,M2,M3,M4,M5,M6,M7,M8,M9")
    parser.add_argument('--jsonPath', dest='jsonPath', default=r"/usr/input_picture_attach/pictureName.json")
    parser.add_argument('--outputDir', dest='outputDir', default=r"/usr/output_dir")
    #
    parser.add_argument('--gpuID', dest='gpuID', type=int, default=0)
    parser.add_argument('--port', dest='port', type=int, default=45452)
    parser.add_argument('--gpuRatio', dest='gpuRatio', type=float, default=0.3)
    parser.add_argument('--host', dest='host', type=str, default='127.0.0.1')
    parser.add_argument('--logID', dest='logID', type=str, default=str(uuid.uuid1())[:6])
    parser.add_argument('--objName', dest='objName', type=str, default='')
    #
    args = parser.parse_args()
    return args


if __name__ == '__main__':

    start_time = time.time()

    args = parse_args()

    scriptName = os.path.basename(__file__).split('.')[0]

    img_dir = r"/usr/input_picture"
    save_dir = r"/usr/output_dir/fzc_res"

    img_path_list = list(
        FileOperationUtil.re_all_file(img_dir, lambda x: str(x).endswith(('.jpg', '.JPG', '.png', '.PNG'))))

    model_fzc_1 = FasterDetectionPytorch(args, "fzc_step_one", scriptName)
    model_fzc_1.model_restore()
    model_fzc_2 = VggClassify(args, "fzc_step_new", scriptName)
    model_fzc_2.model_restore()

    # dete
    # pool = ThreadPool(10)
    # pool.map(detect_fzc, img_path_list)
    # pool.close()
    # pool.join()
    #

    for index, each_img_path in enumerate(img_path_list):
        print("*", index, each_img_path)

        detect_fzc(each_img_path)

    end_time = time.time()
    print("* check img {0} use time {1}".format(len(img_path_list), end_time - start_time))






