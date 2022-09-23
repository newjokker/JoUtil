# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import argparse
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil


# todo ucd 自动下载指定的 数据集

# todo ucd 将下载的数据集解析为 xml（已经有对应的 xml 的不进行解析）

# todo python 脚本将 xml 转为 对应的 yolo 训练 txt

# todo 解析 ucd 拿到用到的 label，生成对应的数据，生成 yaml 文件，存放在指定的目录

# todo 进行训练并实时打印出日志，docker run 的时候改为 后台运行，但是可以查看输出 日志的形式

"""
* /usr/ucd_cache , 所有的图片的存放目录, 因为 ucd 默认的缓存文件夹和其他缓存文件不在一个地方

* /usr/yolo_train/xml_dir
* /usr/yolo_train/txt_dir （train | val） , yolo 训练使用的 txt 的目录
* /usr/yolo_train/train.yaml  指定的存放目录
"""

def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='run model')
    parser.add_argument('--xml_dir', dest='xml_dir', type=str)
    parser.add_argument('--txt_dir', dest='txt_dir', type=str)
    parser.add_argument('--label_list', dest='label_list', type=str)
    assign_args = parser.parse_args()
    return assign_args


def xml_to_txt(xml_path, txt_path, label_dict):
    """将 xml 转为 yolo 训练需要的 json"""
    dete_res = DeteRes(xml_path)
    w = dete_res.width
    h = dete_res.height

    if (w < 1) or (h < 1):
        raise ValueError(f"w or h error : {xml_path}")

    dw = 1./w
    dh = 1./h

    with open(txt_path, "w") as txt_file:
        for each_obj in dete_res:
            x = ((each_obj.x1 + each_obj.x2) / 2.0 - 1) * dw
            y = ((each_obj.y1 + each_obj.y2) / 2.0 - 1) * dh
            w = (each_obj.x2 - each_obj.x1) * dw
            h = (each_obj.y2 - each_obj.y1) * dh

            if (x > 1):
                raise ValueError(f"x > 1, x : {x}, width : {w}")

            if (y > 1):
                raise ValueError(f"y > 1, y : {y}, height : {h}")

            label_index = label_dict[each_obj.tag]
            txt_file.write(f"{label_index} {x} {y} {w} {h}\n")

def convert_xml_to_yolo_format(xml_dir, save_dir, label_dict):
    """将 xml 转为 yolo 训练的 txt 格式"""

    os.makedirs(save_dir, exist_ok=True)
    index = 0
    for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=[".xml"]):
        index += 1
        print(f"{index}, {each_xml_path}")
        each_name = FileOperationUtil.bang_path(each_xml_path)[1]
        each_txt_path = os.path.join(save_dir, each_name + ".txt")

        if os.path.exists(each_txt_path):
            print(f"file exists, ignore, {each_xml_path}")
        else:
            xml_to_txt(each_xml_path, each_txt_path, label_dict)



if __name__ == "__main__":

    args = parse_args()

    labelListStr = args.label_list
    labelList = labelListStr.split(",")
    labelDict = {}

    index = 0
    for each_label in labelList:
        each_label = each_label.strip()
        labelDict[each_label] = index
        index += 1

    convert_xml_to_yolo_format(args.xml_dir, args.txt_dir, labelDict)








