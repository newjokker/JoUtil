# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.txkj.parseXml import parse_xml
from JoTools.operateResXml import OperateResXml
from JoTools.detectionResult import OperateDeteRes, DeteRes
from JoTools.for_csdn.word_pic.word_pic import WordImage
from PIL import Image

# OperateResXml.show_class_count(r"C:\data\fzc_优化相关资料\dataset_fzc\012_增加step_2标图范围，标图数量\fzc_single_add_35KV\train")
# OperateResXml.show_class_count(r"/home/ldq/EfficientDetDetctionTest/Yet-Another-EfficientDet-Pytorch/datasets/fzc_single/train")


# a = OperateDeteRes()
#
# # check_res = a.cal_model_acc(r"C:\Users\14271\Desktop\优化开口销第二步\000_标准测试集\内蒙-南平【标准】Lm3cls测试集\NM_standerd_xml",
# #                             r"C:\Users\14271\Desktop\优化开口销第二步\003_检测结果\result_faster",
# #                             r"C:\Users\14271\Desktop\优化开口销第二步\000_标准测试集\内蒙-南平【标准】Lm3cls测试集\NM_standerd_pic",
# #                             r"C:\Users\14271\Desktop\save_res_2")
#
#
#
# OperateResXml.show_class_count(r"C:\Users\14271\Desktop\优化开口销第二步\000_标准测试集\内蒙-南平【标准】Lm3cls测试集\NM_standerd_xml")


# for each in check_res.items():
#     print(each)
#


# ratio = 2  # 图像缩小的比例
# img_path = r"C:\Users\14271\Desktop\test.png"
# save_path = r'C:\Users\14271\Desktop\beer2.jpg'
# # -------------------------------------------------------------------------------------
#
# img = Image.open(img_path)
# width, height = img.size
# new_width, new_height = int(width / ratio), int(height / ratio)
#
# a = WordImage(img_path, new_size=(new_width, new_height), save_path=save_path)
# a.do_process()


img_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\015_防振锤准备使用faster训练_在原图上标注\007_对新增加的数据整体进行纠偏\自己拍的照片\img"
xml_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\015_防振锤准备使用faster训练_在原图上标注\007_对新增加的数据整体进行纠偏\自己拍的照片\img"
save_dir = r"C:\data\fzc_优化相关资料\dataset_fzc\015_防振锤准备使用faster训练_在原图上标注\007_对新增加的数据整体进行纠偏\自己拍的照片\crop"

# a = DeteRes(xml_path=r"C:\Users\14271\Desktop\yuantu.xml")

# res = a.do_fzc_format()



OperateDeteRes.crop_imgs(img_dir, xml_dir, save_dir=save_dir, split_by_tag=True)
