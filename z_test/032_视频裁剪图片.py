# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.utils.VideoUtilCV import VideoUtilCV
from JoTools.utils.FileOperationUtil import FileOperationUtil


vedio_dir = r"C:\Users\14271\Desktop\人脸识别\视频"
save_dir = r"C:\Users\14271\Desktop\del\cut_from_vedio"
sep=30
start_index=0


for each_vedio_path in FileOperationUtil.re_all_file(vedio_dir, lambda x:str(x).endswith(('.mp4', '.MP4'))):
    print(each_vedio_path)
    VideoUtilCV.get_img_from_vedio(vedio_path=each_vedio_path, save_dir=save_dir, sep=30)

