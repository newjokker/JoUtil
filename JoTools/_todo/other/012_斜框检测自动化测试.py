# -*- coding: utf-8  -*-
# -*- author: jokker -*-

"""

'PGuaBan',
'ZGuaBan',
'Sanjiaoban',
'UBGuaBan',
'UGuaHuan',
'ULuoShuan',
'ZHGuaHuan',
'Zhongchui',
'XuanChuiXianJia',
'ZBDGuaBan',
'YuJiaoShiXJ'

"""

from JoTools.txkjRes.deteRes import DeteRes
from JoTools.operateDeteRes import OperateDeteRes, DeteAcc


# assign_img_dir = r"C:\Users\14271\Desktop\斜框检测测试集\img_xml"
assign_img_dir = r""
standard_xml_dir = r"C:\Users\14271\Desktop\斜框检测测试集\img_xml"
customized_xml_dir = r"C:\Users\14271\Desktop\斜框检测测试集\test_xml"
# save_dir = r"C:\Users\14271\Desktop\斜框检测测试集\res"
save_dir = r""

a = DeteAcc()
a.iou_thershold = 0.4
res = a.cal_model_acc(standard_xml_dir, customized_xml_dir, assign_img_dir, save_dir=save_dir)

for each in res.items():
    print(each)

print(r"-"*100)

for each in a.cal_acc_rec(res).items():
    print(each)

