# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.txkjRes.deteXml import parse_xml_as_txt
from JoTools.utils.FileOperationUtil import FileOperationUtil
from PIL import Image
import time

def is_format_xml(xml_info:dict, w, h, size_th):

    if not len(xml_info['object']):
        return False

    if xml_info['size']['width'] != w or xml_info['size']['height'] != h:
        return False

    for each_dete_obj in xml_info['object']:
        if each_dete_obj['bndbox']['xmax'] - each_dete_obj['bndbox']['xmin'] < size_th:
            return False

        if each_dete_obj['bndbox']['ymax'] - each_dete_obj['bndbox']['ymin'] < size_th:
            return False
    return True



if __name__ == "__main__":


    xml_dir = r"/home/ldq/input_dir/del_test_all/南网香港"
    img_dir = r"/home/ldq/input_dir/del_test_all/南网香港"
    error_dir = r"/home/ldq/input_dir/rubbish"
    error_path_list = []
    correct_path_set = set()
    SIZE_TH = 10
    start_time = time.time()

    for index, each_img_path in enumerate(FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg', ".JPG"])):
        each_xml_path = os.path.join(xml_dir, FileOperationUtil.bang_path(each_img_path)[1] + '.xml')
        print(f"{index} , {time.time() - start_time}: {each_img_path}")

        if not os.path.exists(each_xml_path):
            print(f"* img or xml has sth wrong : {each_img_path}")
            continue

        W, H = Image.open(each_img_path).size
        XML_info = parse_xml_as_txt(each_xml_path)

        if not is_format_xml(XML_info, W, H, SIZE_TH):
            print(f"* img or xml has sth wrong : {each_img_path}")
        else:
            correct_path_set.add(each_img_path)
            correct_path_set.add(each_xml_path)

    # 清理其他文件
    for each_file_path in FileOperationUtil.re_all_file(img_dir):
        if each_file_path not in correct_path_set:
            error_path_list.append(each_file_path)

    if xml_dir != img_dir:
        for each_file_path in FileOperationUtil.re_all_file(xml_dir):
            if each_file_path not in correct_path_set:
                error_path_list.append(each_file_path)

    FileOperationUtil.move_file_to_folder(error_path_list, error_dir, is_clicp=True)







