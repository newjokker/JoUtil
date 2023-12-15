# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import os
import yaml
import argparse
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='run model')
    parser.add_argument('--yaml_path', dest='yaml_path', type=str)
    parser.add_argument('--label_list', dest='label_list', type=str)
    assign_args = parser.parse_args()
    return assign_args

def get_yaml(yaml_path, label_list, img_dir=None, label_dir=None):

    if img_dir is None:
        img_dir = r"/usr/ucd_cache/img_cache"

    if label_dir is None:
        label_dir = r"/usr/yolo_train/txt_dir"

    context = dict()
    with open(yaml_path, "w", encoding="utf-8") as f:
        context["path"] = img_dir
        context["train"] = [img_dir]
        context["val"] = [img_dir]
        context["train_label"] = [os.path.join(label_dir, "train")]
        context["val_label"] = [os.path.join(label_dir, "val")]
        context["nc"] = len(label_list)
        # tags
        context["names"] = {}
        for index, each_tag in enumerate(label_list):
            context["names"][index] = each_tag
        yaml.dump(context, f)


if __name__ == "__main__":

    args = parse_args()
    label_list_str = args.label_list
    labelList = label_list_str.split(",")
    yamlPath = args.yaml_path

    get_yaml(yamlPath, labelList)
