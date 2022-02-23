# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# refer : https://geek-docs.com/python/python-tutorial/python-argparse.html

# 必须填写的参数，required
# parser.add_argument('--name', required=True)

# dest选项为参数指定名称。 如果未给出，则从选项中推断出来
# parser.add_argument('-n', dest='now', action='store_true', help="shows now")

# type 指定参数的类型，但是不知道 bool 类型为什么老是传给我 字符串类型
# parser.add_argument('-n', type=int, required=True, help="define the number of random integers")

# default 默认值选项
# parser.add_argument('-b', type=int, required=True, help="defines the base value")

# metavar选项为错误的期望值命名，并提供帮助输出
# fixme 知道可能与什么参数混淆，所以提前指定错误的期望值，并提供帮助
# parser.add_argument('-v', type=int, required=True, metavar='value', help="computes cube for the given value")

# append操作允许对重复选项进行分组
# parser.add_argument('-n', '--name', dest='names', action='append', help="provides names to greet")

# nargs指定应使用的命令行参数的数量。
# 需要在 -n 参数后输入两个值，两个值用 空格分开 ，当不是两个值的时候会报错，解析后是一个列表
# parser.add_argument('chars', type=str, nargs=2, metavar='c', help='starting and ending character')

# choices选项将参数限制为给定列表
# todo 这个看着相当有用，需要进行测试
# parser.add_argument('--now', dest='format', choices=['std', 'iso', 'unix', 'tz'], help="shows datetime in given format")

# type 指定要输入的类型，命令行输入的时候指定为 bool 值会一直显示为 True，因为会被认为输入的是字符串
# 可以使用指定 choices=['True', 'False'] 然后解析到字符串之后 eval() 操作解决
# parser.add_argument('-n', '--name', help='you means name?', nargs=2, type=bool)



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





    pass





