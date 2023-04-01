# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
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
    img_dir = r"C:\Users\14271\Desktop\del\del"
    save_dir = r"C:\Users\14271\Desktop\img_split"
    # -----------------------------------------------------


    save_path_0 = os.path.join(save_dir, "0")
    save_path_1 = os.path.join(save_dir, "1")
    save_path_2 = os.path.join(save_dir, "2")

    os.makedirs(save_path_0, exist_ok=True)
    os.makedirs(save_path_1, exist_ok=True)
    os.makedirs(save_path_2, exist_ok=True)


    img_map = {"0":[], "1":[], "2":[]}
    for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=[".jpg", ".JPG", ".png", ".PNG"]):
        each_name = FileOperationUtil.bang_path(each_img_path)[1]
        # FIXME 这边比 ubuntu 运行的版本少了 decode 看看分出来的结果是不是一样的
        md5_str = HashLibUtil.get_str_md5(each_name)
        index = get_index_from_md5(md5_str)
        img_map[str(index)].append(each_img_path)

    FileOperationUtil.move_file_to_folder(img_map["0"], save_path_0, is_clicp=True)
    FileOperationUtil.move_file_to_folder(img_map["1"], save_path_1, is_clicp=True)
    FileOperationUtil.move_file_to_folder(img_map["2"], save_path_2, is_clicp=True)

