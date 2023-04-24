# -*- coding: utf-8  -*-
# -*- author: jokker -*-
import os.path
import sys
import argparse
from JoTools.txkjRes.deteRes import DeteRes,DeteObj
from JoTools.utils.FileOperationUtil import FileOperationUtil

xml_dir = r"/home/suanfa-1/lz/datasets/临时文件夹/suzhouxml"
save_dir = r"/home/suanfa-1/lz/datasets/临时文件夹/new_xml"

index = 0
for each_xml_path in FileOperationUtil.re_all_file(xml_dir, endswitch=['.xml']):

    # print(index, each_xml_path)
    a = DeteRes(each_xml_path)
    a.angle_obj_to_obj()

    md5 = HashLibUtil.get_file_md5(each_img_path)

    a.filter_by_tags(need_tag=['r_y', 'ss_jgt', 'aqm_pd', 'zz_cx', 'ss_snt', 'r_tx', 'ygbx_zc', 'aqm_wpd', 'hbs_zc', 'bxd_wsy', 'bxd_zc', 'aqm_wzqpd', 'hbs_yc', 'hbs_wsy', 'scq_zc', 'aqd_wsy', 'r_pp', 'aqm_zqpd', 'ss_ggt', 'r_ts', 'wgxw_cy', 'wgxw_dsj', 'zsq_wpd'])

    a.save_to_xml(os.path.join(save_dir, os.path.split(each_xml_path)[1]))

    index += 1
    # print(index, each_xml_path)






