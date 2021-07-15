# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import sys
import argparse
from JoTools.operateDeteRes import OperateDeteRes


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='run model')
    parser.add_argument('--xml_dir', dest='xml_dir',type=str)
    assign_args = parser.parse_args()
    return assign_args


if __name__ == "__main__":

    if len(sys.argv) > 1:
        args = parse_args()
        print(args.xml_dir)
        OperateDeteRes.get_class_count(args.xml_dir, print_count=True)
    else:
        xml_dir = r"C:\Users\14271\Desktop\del\v1.2.5.0_new"
        OperateDeteRes.get_class_count(xml_dir, print_count=True)

