# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import time
import cv2
import numpy as np
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil
from multiprocessing import Pool
from functools import partial


def resize_one_img_xml(save_dir, resize_ratio, img_xml):
    """将一张训练图片进行 resize"""
    # 解析读到的数据
    img_path, xml_path = img_xml
    #
    a = DeteRes(xml_path)
    #
    if (not os.path.exists(img_path)) or (not os.path.exists(xml_path)):
        return
    #
    if len(a) < 1:
        return
    #
    im = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)
    im_height, im_width = im.shape[:2]
    im_height_new, im_width_new = int(im_height * resize_ratio), int(im_width * resize_ratio)
    im_new = cv2.resize(im, (im_width_new, im_height_new))
    #
    # a.height = im_height_new
    # a.width = im_width_new
    # a.img_path =
    # 将每一个 obj 进行 resize
    for each_obj in a:
        each_obj.x1 = max(1, int(each_obj.x1 * resize_ratio))
        each_obj.x2 = min(im_width_new - 1, int(each_obj.x2 * resize_ratio))
        each_obj.y1 = max(1, int(each_obj.y1 * resize_ratio))
        each_obj.y2 = min(im_height_new - 1, int(each_obj.y2 * resize_ratio))
    # 保存 img
    save_img_path = os.path.join(save_dir, 'JPEGImages', FileOperationUtil.bang_path(xml_path)[1] + '.jpg')
    cv2.imwrite(save_img_path, im_new)
    # 保存 xml
    a.img_path = save_img_path
    save_xml_path = os.path.join(save_dir, 'Annotations', FileOperationUtil.bang_path(xml_path)[1] + '.xml')
    a.save_to_xml(save_xml_path)


def resize_train_data(img_dir, xml_dir, save_dir, resize_ratio=0.5):
    """对训练数据进行resize，resize img 和 xml """

    save_img_dir = os.path.join(save_dir, 'JPEGImages')
    save_xml_dir = os.path.join(save_dir, 'Annotations')
    os.makedirs(save_xml_dir, exist_ok=True)
    os.makedirs(save_img_dir, exist_ok=True)

    index = 0
    for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):
        print(index, each_xml_path)
        index += 1
        each_img_path = os.path.join(img_dir, FileOperationUtil.bang_path(each_xml_path)[1] + '.jpg')
        resize_one_img_xml(save_dir, resize_ratio, (each_img_path, each_xml_path))


if __name__ == "__main__":

    # img_dir = r"C:\Users\14271\Desktop\del\resize\img"
    # xml_dir = r"C:\Users\14271\Desktop\del\resize\xml"
    # save_dir = r"C:\Users\14271\Desktop\del\resize\res"

    xml_dir = r"/home/suanfa-4/ldq/001_train_data/fzc_step_1/Annotations"
    img_dir = r"/home/suanfa-4/ldq/001_train_data/fzc_step_1/JPEGImages"
    save_dir = r"/home/suanfa-4/ldq/001_train_data/fzc_step_1_resize"

    start_time = time.time()

    # OperateDeteRes.resize_train_data(img_dir=img_dir, xml_dir=xml_dir, save_dir=save_dir, resize_ratio=0.2)
    resize_train_data(img_dir=img_dir, xml_dir=xml_dir, save_dir=save_dir, resize_ratio=0.2)

    #
    # save_img_dir = os.path.join(save_dir, 'JPEGImages')
    # save_xml_dir = os.path.join(save_dir, 'Annotations')
    # os.makedirs(save_xml_dir, exist_ok=True)
    # os.makedirs(save_img_dir, exist_ok=True)
    #
    # xml_img_list = []
    # for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):
    #     each_img_path = os.path.join(img_dir, FileOperationUtil.bang_path(each_xml_path)[1] + '.jpg')
    #     xml_img_list.append((each_img_path, each_xml_path))
    #
    # # 并行
    # pool = Pool(processes=4)
    # func = partial(OperateDeteRes.resize_one_img_xml, save_dir, 0.5)
    # pool.map(func, xml_img_list)
    # pool.close()
    # pool.join()

    print("use {0} s".format(time.time() - start_time))


