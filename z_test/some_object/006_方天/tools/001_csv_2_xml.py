# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.CsvUtil import CsvUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil


csv_path = r"C:\Users\14271\Desktop\fangtian_test\result.csv"
img_dir = r"C:\Users\14271\Desktop\fangtian_test\fangtian_nc_kkx"
save_dir = r"C:\Users\14271\Desktop\fangtian_test\xml"


def find_img_path_from_name(img_path_list, img_name):
    """从文件名找到文件路径"""
    for each_img_path in img_path_list:
        if os.path.split(each_img_path)[1] == img_name:
            return each_img_path


if __name__ == "__main__":

    img_path_list = FileOperationUtil.re_all_file(img_dir, endswitch=[".jpg", ".JPG", ".png", ".PNG"])
    csv_info = CsvUtil.read_csv_to_list(csv_path)[1:]
    dete_res_dict = {}

    # get dete res
    for each in csv_info:
        img_name = each[0]
        code, score, xmin, ymin, xmax, ymax = each[1], each[2], each[3], each[4], each[5], each[6]
        #
        if img_name not in dete_res_dict:
            dete_res = DeteRes()
            dete_res.img_path = find_img_path_from_name(img_path_list, img_name)
            dete_res_dict[img_name] = dete_res
        else:
            dete_res = dete_res_dict[img_name]
        # add obj
        dete_res.add_obj(x1=xmin, y1=ymin, x2=xmax, y2=ymax, tag=code, conf=float(score))

    # save dete res to xml
    for each_img_name in dete_res_dict:
        each_dete_res = dete_res_dict[each_img_name]
        save_xml_path = os.path.join(save_dir, each_img_name[:-4] + '.xml')
        each_dete_res.save_to_xml(save_xml_path)















