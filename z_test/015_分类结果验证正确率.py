# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.operateDeteRes import OperateDeteRes


# stand_img_dir = r"C:\data\fzc_优化相关资料\防振锤优化\000_标准分类测试集"
stand_img_dir = r"C:\data\fzc_优化相关资料\防振锤优化\000_标准分类测试集\crop_add_broken"
# custom_img_dir = r"C:\Users\14271\Desktop\fzc分类验证结果\fzc_test_res_001"
custom_img_dir = r"C:\Users\14271\Desktop\fzc分类验证结果\fzc_test_res_006"

OperateDeteRes.cal_acc_classify(stand_img_dir, custom_img_dir)
