# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.operateDeteRes import OperateDeteRes
# from JoTools.operateResXml import OperateResXml
# from JoTools.txkj.parseXml import parse_xml
# from JoTools.for_csdn.word_pic.word_pic import WordImage
# from JoTools.for_csdn.the_art_of_war.the_art_of_war import TheArtOfWar
# from JoTools.utils.FileOperationUtil import FileOperationUtil
# from JoTools.operateResXml import OperateResXml
# # from JoTools.txkj.databaseUtil import CocoDatabaseUtil
# from JoTools.utils.HashlibUtil import HashLibUtil
# import copy



dete_res_standard = r"C:\Users\14271\Desktop\优化开口销第二步\000_标准测试集\NM_standerd_xml"
# dete_res_customized = r"C:\Users\14271\Desktop\kkx检测结果对比\002_仅对比第二步结果\002_新模型检测结果\kkx_step_2_crop_0.35_22"
# dete_res_customized = r"C:\Users\14271\Desktop\kkx检测结果对比\001_全流程结果对比\result_normal"
dete_res_customized = r"C:\Users\14271\Desktop\result_不识别其他类型得到的最后结果"
# dete_res_customized = r"C:\Users\14271\Desktop\kkx检测结果对比\002_仅对比第二步结果\002_新模型检测结果\kkx_step_2_crop_0.4_22"
# assign_img_path = r"C:\Users\14271\Desktop\优化开口销第二步\000_标准测试集\NM_standerd_pic"
assign_img_path = r""
# save_path=r"C:\Users\14271\Desktop\old_res"
save_path= r""


a = OperateDeteRes()
a.iou_thershold = 0.2
res = a.cal_model_acc(standard_xml_dir=dete_res_standard, customized_xml_dir=dete_res_customized, assign_img_dir=assign_img_path, save_dir=save_path)

for each in res.items():
    print(each)

res_2 = OperateDeteRes.cal_acc_rec(res, ['Xnormal', 'K', 'Lm', 'kkxTC'])
print(res_2)

# a = [('extra_Xnormal', 929), ('correct_Xnormal', 4858),
# ('correct_Lm', 3654), ('extra_K', 519),
# ('mistake_K-Xnormal', 41), ('miss_K', 72), ('miss_Xnormal', 681), ('miss_Lm', 643), ('mistake_Lm-Xnormal', 148),
# ('mistake_Xnormal-kkxTC', 111), ('extra_Lm', 656),
# ('correct_K', 254), ('mistake_Xnormal-K', 80), ('mistake_Xnormal-Lm', 28), ('extra_kkxTC', 20),
# ('mistake_Lm-K', 15), ('mistake_K-Lm', 5), ('mistake_Lm-kkxTC', 1)]
#
# a = dict(a)
#
# b = OperateDeteRes.cal_acc_rec(a)
#
# print(b)

# --------------------------------------------------------------


