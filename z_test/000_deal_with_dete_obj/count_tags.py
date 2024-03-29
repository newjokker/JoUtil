# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import sys
import argparse
from JoTools.operateDeteRes import OperateDeteRes
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
        # xml_dir = r"C:\Users\14271\Desktop\save_res"
        # xml_dir = r"C:\Users\14271\Desktop\docker-0.0.1\save_res"
        # xml_dir = r"C:\Users\14271\Desktop\result_xml"
        xml_dir = r"C:\Users\14271\Desktop\xml_recommend\Annonations_random"
        res = OperateDeteRes.get_class_count(xml_dir, print_count=True)

        print(len(list(res.keys())))

