# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import argparse
import sys
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.TxtUtil import TxtUtil
from JoTools.utils.PrintUtil import PrintUtil


def get_img_txt(img_dir, txt_path):
    img_path_list = []
    for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg', '.JPG', '.png', '.PNG']):
        img_path_list.append([each_img_path])
    TxtUtil.write_table_to_txt(img_path_list, txt_path, end_line='\n')


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='run model')
    parser.add_argument('--img_dir', dest='img_dir',type=str)
    parser.add_argument('--txt_path', dest='txt_path',type=str, default=None)
    assign_args = parser.parse_args()
    return assign_args


if __name__ == "__main__":

    if len(sys.argv) > 1:
        args = parse_args()
        PrintUtil.print(args)

        get_img_txt(img_dir=args.img_dir, txt_path=args.txt_path)
    else:
        img_dir = r""
        txt_path = r""
        get_img_txt(img_dir=img_dir, txt_path=txt_path)

