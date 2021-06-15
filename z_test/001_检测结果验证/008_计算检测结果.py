# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.operateDeteRes import OperateDeteRes, DeteAcc
from JoTools.txkjRes.deteRes import DeteRes

dete_res_standard = r"C:\data\fzc_优化相关资料\dataset_fzc\000_0_标准测试集\xml"
# dete_res_standard = r"C:\Users\14271\Desktop\fzc_多版本对比\xml_v0.2.4.0"
dete_res_customized = r"C:\Users\14271\Desktop\fzc_多版本对比\xml_v0.2.3-C"
assign_img_path = r"C:\data\fzc_优化相关资料\dataset_fzc\000_0_标准测试集\img"
save_path= r"C:\Users\14271\Desktop\fzc_多版本对比\compare_v0.2.3-C"


a = DeteAcc()
a.iou_thershold = 0.4
res = a.cal_model_acc(standard_xml_dir=dete_res_standard, customized_xml_dir=dete_res_customized, assign_img_dir=assign_img_path, save_dir=save_path, assign_conf=0.1, save_img=False, save_xml=True)


res_2 = a.cal_acc_rec(res)


for each in res.items():
    print(each)

print('-'*50)

for each in res_2.items():
    print(each)

