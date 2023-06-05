# -*- coding: utf-8 -*-
import os
import cv2  ##加载OpenCV模块

import shutil
from JoTools.utils.VideoUtilCV import VideoUtilCV
from JoTools.utils.FileOperationUtil import FileOperationUtil

vedio_dir = r"F:\0530\0522终端采集设备视频收集\电池欠压换表（丰台六里桥）\new"
save_dir = r"C:\Users\14271\Desktop\temp"


for each_vedio_path in FileOperationUtil.re_all_file(vedio_dir, endswitch=[".mp4", ".MOV", ".AVI"]):

    print("* ", each_vedio_path)
    dir_name, file_name = os.path.split(each_vedio_path)
    file_name, suffix = os.path.splitext(file_name)
    save_folder = os.path.join(save_dir, file_name)

    if os.path.exists(save_folder):
        shutil.rmtree(save_folder)
        os.makedirs(save_folder)
    else:
        os.makedirs(save_folder)

    for each in VideoUtilCV.get_img_from_vedio(each_vedio_path, save_folder, sep=10, start_index=0):
        print(each)

















