# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import sys
import argparse
from JoTools.operateDeteRes import OperateDeteRes, DeteAcc
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.PrintUtil import PrintUtil

dete_res_standard = r"C:\Users\14271\Desktop\new_gt"
# dete_res_customized = r"C:\Users\14271\Desktop\fzcRust_v1.1.1.0"
dete_res_customized = r"C:\Users\14271\Desktop\fzcRust_v1.0.3.0"
assign_img_path = r""
save_path = r""

a.iou_thershold = 0.3

for each_conf in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99]:
    res = a.cal_model_acc(standard_xml_dir=dete_res_standard, customized_xml_dir=dete_res_customized, assign_img_dir=assign_img_path, save_dir=save_path, save_img=False, save_xml=True, assign_conf=each_conf)
    res_2 = a.cal_acc_rec(res)
    print('-'*80)
    PrintUtil.print(res_2)