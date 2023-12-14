# -*- coding: utf-8 -*-
import os
import cv2  ##加载OpenCV模块

import shutil
from JoTools.utils.VideoUtilCV import VideoUtilCV
from JoTools.utils.FileOperationUtil import FileOperationUtil

# 两天数据都在里面了，我怕麻烦，复制到一起了
# for name in ["14_12", "15_10", "15_12", "16_10", "16_12"]:
for name in ["16", "17"]:
# for name in ["14", "15"]:

    vedio_dir = r"G:\TX00100012\2023-06-30\{0}".format(name)
    save_dir = r"C:\Users\14271\Desktop\feihua_0630\012_0630_{0}".format(name)

    # vedio_dir = r"C:\Users\14271\Desktop\feihua_0626\012_0626_10\no_jyg"
    # save_dir = r"C:\Users\14271\Desktop\feihua_0626\012_0626_10\no_jyg"


    os.makedirs(save_dir, exist_ok=True)

    for each_vedio_path in FileOperationUtil.re_all_file(vedio_dir, endswitch=[".mp4", ".MOV", ".AVI", ".MP4", ".m3u8", ".ts"]):

        try:
            print("* ", each_vedio_path)
            dir_name, file_name = os.path.split(each_vedio_path)
            file_name, suffix = os.path.splitext(file_name)
            # save_folder = os.path.join(save_dir, file_name)

            # if os.path.exists(save_folder):
            #     shutil.rmtree(save_folder)
            #     os.makedirs(save_folder)
            # else:
            #     os.makedirs(save_folder)

            index = 0
            for each in VideoUtilCV.get_img_from_vedio(each_vedio_path, save_dir, sep=1, start_index=0):
                index += 1
                print(each)
                if(index > 200):
                    break

        except Exception as e:
            print(e)


