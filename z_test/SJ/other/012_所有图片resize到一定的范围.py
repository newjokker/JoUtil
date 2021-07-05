# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import cv2
import os
import shutil
from JoTools.utils.FileOperationUtil import FileOperationUtil



img_dir = r"/home/suanfa-3/ldq/001_test_data/fzc_fnormal"
min_size = 1500
save_dir = r"/home/suanfa-3/ldq/001_test_data/fzc_fnormal_resize"

for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg', '.JPG']):
    im = cv2.imread(each_img_path)
    im_height, im_width = im.shape[:2]

    new_img_path = os.path.join(save_dir, FileOperationUtil.bang_path(each_img_path)[1] + '.jpg')

    if (im_height > 1500) or (im_width > 1500):
        ratio = max(im_width, im_height) / 1500
        new_height = int(im_height * ratio)
        new_width = int(im_width * ratio)
        im = cv2.resize(im, (im_width, im_height))
        cv2.imwrite(new_img_path, im)
    else:
        shutil.copy(each_img_path, new_img_path)





