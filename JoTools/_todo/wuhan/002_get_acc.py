

from JoTools.operateDeteRes import DeteAcc
from JoTools.operateDeteRes import OperateDeteRes


dete_res_standard = r""
dete_res_customized = r""
assign_img_path = r""
save_path = r""


a = DeteAcc()
res = a.cal_model_acc(dete_res_standard, dete_res_customized, assign_img_path, save_path)

acc = DeteAcc.cal_acc_rec(res)

for each in acc.items():
    print(each)




