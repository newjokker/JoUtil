# -*- coding: utf-8 -*-
import os
import cv2  ##加载OpenCV模块

import shutil
from JoTools.utils.VideoUtilCV import VideoUtilCV
from JoTools.utils.FileOperationUtil import FileOperationUtil






def vedio_to_img(vedio_dir, save_dir, max_img_count_one_vedio=200):

    # vedio_dir = r"G:\北京飞华\飞华_0616_12\09"
    # save_dir = r"C:\Users\14271\Desktop\temp\pic_feihua_0616_12_09"

    os.makedirs(save_dir, exist_ok=True)

    for each_vedio_path in FileOperationUtil.re_all_file(vedio_dir, endswitch=[".mp4", ".MOV", ".AVI", ".MP4", ".m3u8", ".ts"]):
        try:
            print("* ", each_vedio_path)
            dir_name, file_name = os.path.split(each_vedio_path)
            file_name, suffix = os.path.splitext(file_name)
            save_folder = os.path.join(save_dir, file_name)

            if os.path.exists(save_folder):
                shutil.rmtree(save_folder)
                os.makedirs(save_folder)
            else:
                os.makedirs(save_folder)

            index = 0
            for each in VideoUtilCV.get_img_from_vedio(each_vedio_path, save_folder, sep=1, start_index=0):
                index += 1
                print(each)
                if(index > max_img_count_one_vedio):
                    break

        except Exception as e:
            print(e)




if __name__ == "__main__":


    vedio_to_img(r"G:\北京飞华\飞华_0616_12\10", r"C:\Users\14271\Desktop\temp\pic_feihua_0616_12_10")
    vedio_to_img(r"G:\北京飞华\飞华_0616_12\11", r"C:\Users\14271\Desktop\temp\pic_feihua_0616_12_11")
    vedio_to_img(r"G:\北京飞华\飞华_0616_12\12", r"C:\Users\14271\Desktop\temp\pic_feihua_0616_12_12")
    vedio_to_img(r"G:\北京飞华\飞华_0616_12\13", r"C:\Users\14271\Desktop\temp\pic_feihua_0616_12_13")
    vedio_to_img(r"G:\北京飞华\飞华_0616_12\14", r"C:\Users\14271\Desktop\temp\pic_feihua_0616_12_14")
    vedio_to_img(r"G:\北京飞华\飞华_0616_12\15", r"C:\Users\14271\Desktop\temp\pic_feihua_0616_12_15")

    vedio_to_img(r"G:\北京飞华\飞华_0616_02\09", r"C:\Users\14271\Desktop\temp\pic_feihua_0616_02_09")
    vedio_to_img(r"G:\北京飞华\飞华_0616_02\10", r"C:\Users\14271\Desktop\temp\pic_feihua_0616_02_10")













