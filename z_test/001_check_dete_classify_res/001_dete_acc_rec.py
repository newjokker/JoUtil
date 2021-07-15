# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import sys
import argparse
from JoTools.operateDeteRes import OperateDeteRes, DeteAcc
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.PrintUtil import PrintUtil


def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='run model')
    parser.add_argument('--standard_dir', dest='standard_dir',type=str)
    parser.add_argument('--customized_dir', dest='customized_dir',type=str)
    parser.add_argument('--img_dir', dest='img_dir',type=str, default="")
    parser.add_argument('--save_dir', dest='save_dir',type=str, default="")
    parser.add_argument('--iou', dest='iou',type=float, default=0.3)
    parser.add_argument('--save_img', dest='save_img',type=bool, default=False)
    parser.add_argument('--save_xml', dest='save_xml',type=bool, default=False)
    parser.add_argument('--assign_conf', dest='assign_conf',type=float, default=None)
    assign_args = parser.parse_args()
    return assign_args


if __name__ == "__main__":

    # python C:\Algo\jo_util\z_test\001_check_dete_classify_res\001_dete_acc_rec.py --standard_dir C:\data\fzc_优化相关资料\dataset_fzc\000_0_标准测试集\Annotations  --customized_dir  C:\Users\14271\Desktop\finally_test
    
    a = DeteAcc()

    if len(sys.argv) > 1:
        # 解析参数
        args = parse_args()
        # 打印信息
        PrintUtil.print(args)
        #
        a.iou_thershold = args.iou
        # 计算各种情况的目标个数
        res = a.cal_model_acc(standard_xml_dir=args.standard_dir, customized_xml_dir=args.customized_dir, assign_img_dir=args.img_dir,
                              save_dir=args.save_dir, save_img=args.save_img, save_xml=args.save_xml, assign_conf=args.assign_conf)
        # 计算正确率，召回率
        res_2 = a.cal_acc_rec(res)

    else:

        dete_res_standard = r"C:\data\fzc_优化相关资料\dataset_fzc\000_0_标准测试集\Annotations"
        dete_res_customized = r"C:\Users\14271\Desktop\finally_test"
        assign_img_path = r"C:\data\fzc_优化相关资料\dataset_fzc\000_0_标准测试集\JPEGImages"
        save_path= r"C:\Users\14271\Desktop\del\v1.2.5.0_new"

        a.iou_thershold = 0.3
        # 计算各种情况的目标个数
        res = a.cal_model_acc(standard_xml_dir=dete_res_standard, customized_xml_dir=dete_res_customized, assign_img_dir=assign_img_path, save_dir=save_path, save_img=False, save_xml=True, assign_conf=0.3)
        # 计算正确率，召回率
        res_2 = a.cal_acc_rec(res)


    PrintUtil.print(res)
    print('-'*30)
    PrintUtil.print(res_2)

