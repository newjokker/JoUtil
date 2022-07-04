# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.utils.FileOperationUtil import FileOperationUtil
import argparse
import time

def analysis_dir(file_dir):
    suffix_map = {}
    for each_file_path in FileOperationUtil.re_all_file(file_dir):
        suffix = FileOperationUtil.bang_path(each_file_path)[2]
        if suffix in suffix_map:
            suffix_map[suffix] += 1
        else:
            suffix_map[suffix] = 1
    sum = 0
    for k,v in suffix_map.items():
        sum += v
        print(f"{str(k).ljust(20, ' ')}, {v}")
        print('-'*40)
    print(f"{'sum'.ljust(20, ' ')}, {sum}")

def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='run model')
    parser.add_argument('--file_dir', dest='file_dir',type=str)
    assign_args = parser.parse_args()
    return assign_args



if __name__ == "__main__":

    args = parse_args()
    start_time = time.time()
    analysis_dir(args.file_dir)
    print(f"use time {time.time() - start_time} s")




