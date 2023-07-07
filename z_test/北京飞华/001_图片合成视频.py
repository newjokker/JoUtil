# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
import cv2  ##加载OpenCV模块

import shutil
from JoTools.utils.VideoUtilCV import VideoUtilCV
from JoTools.utils.FileOperationUtil import FileOperationUtil

vedio_dir = r"C:\Users\14271\Desktop\cut_ori_dete"
save_path = r"C:\Users\14271\Desktop\cut_ori_dete.mp4"


img_path_list = list(FileOperationUtil.re_all_file(vedio_dir, endswitch=[".jpg", ".JPG", ".png", ".PNG"]))

VideoUtilCV.write_vedio(img_path_list, save_path, assign_fps=20)






