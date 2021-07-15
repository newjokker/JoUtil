# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import sys
import argparse
from JoTools.operateDeteRes import OperateDeteRes


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='run model')
    parser.add_argument('--img_dir', dest='img_dir',type=str)
    parser.add_argument('--xml_dir', dest='xml_dir',type=str)
    parser.add_argument('--save_dir', dest='save_dir',type=str)
    parser.add_argument('--split_by_tag', dest='split_by_tag',type=str, default=True)
    parser.add_argument('--augment_parameter', dest='augment_parameter',type=list, default=[0,0,0,0])
    parser.add_argument('--include_tag_list', dest='include_tag_list',type=str, default=None)
    parser.add_argument('--exclude_tag_list', dest='exclude_tag_list',type=str, default=None)
    assign_args = parser.parse_args()
    return assign_args


if __name__ == "__main__":


    if len(sys.argv) > 1:
        args = parse_args()

        if args.exclude_tag_list:
            exclude_tag_list = args.exclude_tag_list.split(',')
        else:
            exclude_tag_list = None

        if args.include_tag_list:
            include_tag_list = args.include_tag_list.split(',')
        else:
            include_tag_list = None

        OperateDeteRes.crop_imgs(args.img_dir, args.xml_dir, args.save_dir, split_by_tag=args.split_by_tag, augment_parameter=args.augment_parameter,
                                 exclude_tag_list=exclude_tag_list, include_tag_list=include_tag_list)
    else:
        img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_0_标准测试集\JPEGImages"
        xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\000_0_标准测试集\Annotations"
        save_dir = r"C:\Users\14271\Desktop\del\crop"
        OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir, split_by_tag=True, augment_parameter=[0.1, 0.1, 0.1, 0.1], include_tag_list=['fzc_broken'])

