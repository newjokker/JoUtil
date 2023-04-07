# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import shutil

from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.HashlibUtil import HashLibUtil


def get_index_from_md5(md5_str):
    sum_res = 0
    for each in md5_str:
        sum_res += ord(each)
    return sum_res % 3


if __name__ == "__main__":

    # todo 核对 linux 上和 windows 上分出来的结果是否一致


    # -----------------------------------------------------
    img_dir = r"C:\Users\14271\Desktop\img_split\img_all"
    save_dir = r"C:\Users\14271\Desktop\img_split\split"
    # -----------------------------------------------------


    save_path_0 = os.path.join(save_dir, "0")
    save_path_1 = os.path.join(save_dir, "1")
    save_path_2 = os.path.join(save_dir, "2")

    save_path_dict = {"0": save_path_0, "1":save_path_1, "2":save_path_2}

    os.makedirs(save_path_0, exist_ok=True)
    os.makedirs(save_path_1, exist_ok=True)
    os.makedirs(save_path_2, exist_ok=True)


    img_map = {"0":[], "1":[], "2":[]}
    for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=[".jpg", ".JPG", ".png", ".PNG", ".jpeg"]):
        each_name = os.path.split(each_img_path)[1]
        md5_str = HashLibUtil.get_str_md5(each_name)
        index = get_index_from_md5(md5_str)
        each_save_path = os.path.join(save_path_dict[str(index)], each_name + ".jpg")
        shutil.move(each_img_path, each_save_path)
