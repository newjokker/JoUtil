# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.detectionResult import OperateDeteRes

a = OperateDeteRes()

check_res = a.cal_model_acc(r"C:\Users\14271\Desktop\优化开口销第二步\000_标准测试集\内蒙-南平【标准】Lm3cls测试集\NM_standerd_xml",
                            r"C:\Users\14271\Desktop\优化开口销第二步\003_检测结果\result_faster",
                            r"C:\Users\14271\Desktop\优化开口销第二步\000_标准测试集\内蒙-南平【标准】Lm3cls测试集\NM_standerd_pic",
                            r"C:\Users\14271\Desktop\save_res_2")


for each in check_res.items():
    print(each)


