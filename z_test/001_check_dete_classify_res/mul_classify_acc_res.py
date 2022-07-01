# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.operateDeteRes import DeteAcc
from collections import Counter



standard_dir = r"C:\Users\14271\Desktop\del\gt_xml"
customized_dir = r"C:\Users\14271\Desktop\res"


res = DeteAcc.cal_model_acc_mul_classify(standard_dir, customized_dir)

print("correct", res['correct'])
print("miss", res['miss'])
print("extra", res['extra'])

res = DeteAcc.cal_acc_rec_mul_classify(res, tag_list=['person', 'long', 'short', 'hat'])

print(res)