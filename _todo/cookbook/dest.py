# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import argparse


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='run model')
    parser.add_argument('--host', dest='host',type=str,default='192.168.3.101')
    parser.add_argument('--port',dest='port',type=str,default='8084')
    # 传入多个参数中间使用逗号隔开，可以使用参数 nargs 指定参数个数，为 ‘+’ 代表可以任意参数个数
    parser.add_argument('--more', dest='more', nargs='+', help='list')

    parser.add_argument('-n', '--name', metavar='nam', help='you means name?')



    args = parser.parse_args()
    return args


if __name__ == "__main__":

    args = parse_args()
