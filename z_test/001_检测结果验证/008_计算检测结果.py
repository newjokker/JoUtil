# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.operateDeteRes import OperateDeteRes, DeteAcc
from JoTools.txkjRes.deteRes import DeteRes

dete_res_standard = r"C:\Users\14271\Desktop\结果对比\standard"
dete_res_customized = r"C:\Users\14271\Desktop\结果对比\merge_update"
assign_img_path = r""
save_path= r"C:\Users\14271\Desktop\结果对比\compare"


a = DeteAcc()
a.iou_thershold = 0.3
res = a.cal_model_acc(standard_xml_dir=dete_res_standard, customized_xml_dir=dete_res_customized, assign_img_dir=assign_img_path, save_dir=save_path, save_img=False, save_xml=True)


res_2 = a.cal_acc_rec(res)


for each in res.items():
    print(each)

print('-'*50)

for each in res_2.items():
    print(each)

