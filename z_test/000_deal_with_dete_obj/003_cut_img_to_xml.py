# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import sys
import argparse
from JoTools.operateDeteRes import OperateDeteRes
from JoTools.utils.PrintUtil import PrintUtil


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='run model')
    parser.add_argument('--img_dir', dest='img_dir',type=str)
    parser.add_argument('--crop_dir', dest='crop_dir',type=str)
    parser.add_argument('--save_dir', dest='save_dir',type=str)
    parser.add_argument('--split_by_tag', dest='split_by_tag',type=str, default=True)
    parser.add_argument('--augment_parameter', dest='augment_parameter',type=str, default="0,0,0,0")
    parser.add_argument('--include_tag_list', dest='include_tag_list',type=str, default=None)
    parser.add_argument('--exclude_tag_list', dest='exclude_tag_list',type=str, default=None)
    assign_args = parser.parse_args()
    return assign_args


if __name__ == "__main__":


    if len(sys.argv) > 1:
        # 解析参数
        args = parse_args()
        # 打印信息
        PrintUtil.print(args)
        # 执行
        OperateDeteRes.get_xml_from_crop_img(region_img_dir=args.img_dir, crop_dir=args.crop_dir, save_xml_dir=args.save_dir)
        # 打印结果
        OperateDeteRes.get_class_count(args.save_dir, print_count=True)

    else:

        img_dir = r"C:\Users\14271\Desktop\寻找未被发现的fzc_broken\JPEGImages"
        crop_dir = r"C:\Users\14271\Desktop\寻找未被发现的fzc_broken\crop"
        save_dir = r"C:\Users\14271\Desktop\寻找未被发现的fzc_broken\xml"

        OperateDeteRes.get_xml_from_crop_img(region_img_dir=img_dir, crop_dir=crop_dir, save_xml_dir=save_dir)
        OperateDeteRes.get_class_count(save_dir, print_count=True)

