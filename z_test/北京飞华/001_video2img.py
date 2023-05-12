# -*- coding: utf-8 -*-
import os
import cv2  ##加载OpenCV模块

import shutil
from JoTools.utils.VideoUtilCV import VideoUtilCV
from JoTools.utils.FileOperationUtil import FileOperationUtil

vedio_dir = r"C:\Users\14271\Desktop\北京飞华\004_demo_使用的视频\001_原始视频"
save_dir = r"C:\Users\14271\Desktop\temp\demo"


for each_vedio_path in FileOperationUtil.re_all_file(vedio_dir, endswitch=[".mp4"]):

    print("* ", each_vedio_path)
    dir_name, file_name = os.path.split(each_vedio_path)
    file_name, suffix = os.path.splitext(file_name)
    save_folder = os.path.join(save_dir, file_name)

    if os.path.exists(save_folder):
        shutil.rmtree(save_folder)
        os.makedirs(save_folder)
    else:
        os.makedirs(save_folder)

    for each in VideoUtilCV.get_img_from_vedio(each_vedio_path, save_folder, sep=1, start_index=0):
        print(each)

















