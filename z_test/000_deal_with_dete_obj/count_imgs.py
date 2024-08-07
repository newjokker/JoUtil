# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import sys
import argparse
from JoTools.txkjRes.operateDeteRes import OperateDeteRes
from JoTools.utils.PrintUtil import PrintUtil


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='run model')
    parser.add_argument('--img_dir', dest='img_dir',type=str)
    parser.add_argument('--endswitch', dest='endswitch',type=str, default=None)
    assign_args = parser.parse_args()
    return assign_args


if __name__ == "__main__":

    if len(sys.argv) > 1:
        args = parse_args()
        PrintUtil.print(args)

        if not args.endswitch is None:
            endswitch = args.endswitch.split(',')
        else:
            endswitch = None

        OperateDeteRes.count_assign_dir(args.img_dir, endswitc=endswitch)
    else:
        img_dir = r"\\192.168.3.80\数据\root_dir\json_img"
        # OperateDeteRes.count_assign_dir(img_dir, endswitc=['.xml', '.jpg'])
        OperateDeteRes.count_assign_dir(img_dir, endswitc=['.jpg', '.JPG', '.png', '.PNG'])


