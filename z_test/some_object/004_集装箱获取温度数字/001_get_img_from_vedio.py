# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import cv2
from JoTools.utils.VideoUtilCV import VideoUtilCV
from JoTools.utils.FileOperationUtil import FileOperationUtil
import uuid

# # vedio_path = r"D:\AppData\baiduwangpan\视频识别\H121202-2_20210222114626_20210222120540.dav"
# vedio_path = r"D:\AppData\baiduwangpan\视频识别\H121202-2_20210222114626_20210222120540.dav"
# save_dir = r"C:\Users\14271\Desktop\del\crop_vedio"



def get_img_from_vedio(vedio_path, each_save_dir):

    vc = cv2.VideoCapture(vedio_path)
    c=0
    rval=vc.isOpened()

    sep = 120
    while rval:
        c = c + 1
        for i in range(sep):
            rval, frame = vc.read()

        if rval:
            cv2.imwrite(os.path.join(each_save_dir, str(c)+ "_" + str(uuid.uuid1())+'.jpg'),  frame) #命名方式
        else:
            break
    vc.release()



if __name__ == "__main__":

    vedio_dir = r'C:\Users\14271\Desktop\sifang'
    save_dir = r"C:\Users\14271\Desktop\vedio_img"


    for each_vedio_path in FileOperationUtil.re_all_file(vedio_dir, endswitch=[".dav"]):

        folder_name = os.path.split(FileOperationUtil.bang_path(each_vedio_path)[0])[1]

        each_save_dir = os.path.join(save_dir, folder_name)

        os.makedirs(each_save_dir, exist_ok=True)

        get_img_from_vedio(each_vedio_path, each_save_dir)


        print(folder_name)





