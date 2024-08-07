# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import sys
import argparse
from JoTools.txkjRes.operateDeteRes import OperateDeteRes
from JoTools.utils.PrintUtil import PrintUtil


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='run model')
    parser.add_argument('--xml_dir', dest='xml_dir',type=str)
    assign_args = parser.parse_args()
    return assign_args


if __name__ == "__main__":

    if len(sys.argv) > 1:
        args = parse_args()
        PrintUtil.print(args)
        OperateDeteRes.get_class_count(args.xml_dir, print_count=True)
    else:
        # xml_dir = r"C:\Users\14271\Desktop\配网比赛\xml"
        xml_dir = r"C:\Users\14271\Desktop\北京飞华\010_鞋子视频检测\001_视频截图_用于测试\add\img_xml"
        res = OperateDeteRes.get_class_count(xml_dir, print_count=True)

        print(len(list(res.keys())))

