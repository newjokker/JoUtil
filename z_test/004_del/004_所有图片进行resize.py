# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import cv2
from JoTools.utils.FileOperationUtil import FileOperationUtil


img_dir = r"/home/suanfa-5/ldq/002_test_data/data_69G"
region_dir = r"/home/suanfa-5/ldq/002_test_data/69G塔基_未检出"
save_dir = r"/home/suanfa-5/ldq/002_test_data/69G_挑选出"

index = 0
img_list = []
for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg', '.JPG', '.png', '.PNG']):

    print(index, each_img_path)
    index += 1

    region_img_path = os.path.join(region_dir, os.path.split(each_img_path)[1])

    if os.path.exists(region_img_path):
        img_list.append(region_img_path)


FileOperationUtil.move_file_to_folder(img_list, save_dir, is_clicp=True)

    # img = cv2.imread(each_img_path)
    #
    # hight, width = img.shape[:2]
    #
    # img = cv2.resize(img, (int(width/3), int(hight/3)))
    #
    # save_path = os.path.join(save_dir, os.path.split(each_img_path)[1])
    #
    # cv2.imwrite(save_path, img)






