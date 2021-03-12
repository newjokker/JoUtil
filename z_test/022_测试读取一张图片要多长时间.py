# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.DecoratorUtil import DecoratorUtil

img_dir = r"C:\Users\14271\Desktop\10kV_total_data\img"

@DecoratorUtil.time_this
def get_read_time():

    index = 0
    for each_img_path in FileOperationUtil.re_all_file(img_dir, lambda x:str(x).endswith(".jpg")):
        index += 1
        a =  open(each_img_path, 'rb')
        if index >= 100:
            print("over")
            return


get_read_time()
