# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.operateDeteRes import OperateDeteRes, DeteAcc
from JoTools.txkjRes.deteRes import DeteRes

dete_res_standard = r"C:\data\fzc_优化相关资料\dataset_fzc\000_0_标准测试集\Annotations"
dete_res_customized = r"C:\Users\14271\Desktop\fzc_v1.2.5.0_new版本\001_dete_res\fzc_v1.2.5.6-C\xml"
assign_img_path = r"C:\data\fzc_优化相关资料\dataset_fzc\000_0_标准测试集\JPEGImages"
save_path= r"C:\Users\14271\Desktop\fzc_v1.2.5.0_new版本\001_dete_res\fzc_v1.2.5.6-C\compare_xml"


a = DeteAcc()
a.iou_thershold = 0.3
res = a.cal_model_acc(standard_xml_dir=dete_res_standard, customized_xml_dir=dete_res_customized, assign_img_dir=assign_img_path, save_dir=save_path, save_img=False, save_xml=True, assign_conf=0.3)


res_2 = a.cal_acc_rec(res)


for each in res.items():
    print(each)

print('-'*50)

for each in res_2.items():
    print(each)

