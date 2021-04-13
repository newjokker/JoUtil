# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.operateDeteRes import OperateDeteRes, DeteAcc


dete_res_standard = r"./xml_gt"
dete_res_customized = r"./xml_pr"
assign_img_path = r""
save_path= r""


a = DeteAcc()
a.iou_thershold = 0.4
res = a.cal_model_acc(standard_xml_dir=dete_res_standard, customized_xml_dir=dete_res_customized, assign_img_dir=assign_img_path, save_dir=save_path)

res_2 = a.cal_acc_rec(res)


for each in res.items():
    print(each)

print('-'*50)

for each in res_2.items():
    print(each)