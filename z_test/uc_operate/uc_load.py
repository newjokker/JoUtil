# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import requests
from JoTools.txkj.ucDatasetUtil import UCDatasetUtil
from JoTools.utils.JsonUtil import JsonUtil


# CPP 代码的编写

# 将手头的数据生成 ucDataset.json 用于复用

# 想谁便看看就先下载 指定的个数来看

# todo 将转换这块工作也交给服务端去做，这样就不需要在本地下载转化的代码了

# todo 使用的场景，测试代码在不同的服务器上进行倒腾

# todo 测试代码标准化，完善一个测试数据集合，专门用于测试，先不要求测试图片和训练图片分开

# todo 现在容易卡主应该是因为 把推送图片服务 和 其他任务放在一起的缘故,将他们分为两个 服务试试


save_dir = r"C:\Users\14271\Desktop\del\save_img"

a = UCDatasetUtil(r"C:\Users\14271\Desktop\del\test.json", "192.168.3.111", 11101)

# a.save_img_xml_json(save_dir=save_dir, need_img=True, need_json=False, need_xml=True)

# a.check_ucdataset()
#
# a.delete_ucdataset(r"test\nihao91")
#
# a.upload_ucdataset(r"C:\Users\14271\Desktop\test_ucd.json", r"windows_te2st")

# a.from_img_dir(r"/home/suanfa-1/jtm/ST_projects/trained_pros/yolov5_new/train_data/yolo/train/images",
#                r"/home/suanfa-1/jtm/ST_projects/trained_pros/yolov5_new/train_data/yolo/train/prebase_yolo5_0_5_0_train.json")






