# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import requests
import json
import base64
import time
from JoTools.utils.FileOperationUtil import FileOperationUtil



# res = requests.post(url="http://192.168.3.221:12345/defect/pic/discern", data=json.dumps({"fileName": "file_name",
#                                                                                "picOriginName": "pic_name",
#                                                                                "picBase64": ls_f.decode('utf-8'),
#                                                                                "nms": "0.6"}))

time_start = time.time()
use_time = 0
# img_dir = r"C:\Users\14271\Desktop\del\test_data"
img_dir = r"D:\data\001_fzc_优化相关资料\dataset_fzc\000_train_data_step_1\JPEGImages"

for i in range(1):
    index = 0
    for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg']):
        index += 1
        f = open(each_img_path, "rb")
        ls_f = base64.b64encode(f.read())
        ls_f_str = ls_f.decode('utf-8')

        time_s = time.time()
        res = requests.post(url="http://192.168.3.221:1234/defect/pic/discern",
                            data=json.dumps({"fileName": FileOperationUtil.bang_path(each_img_path)[1],
                                             "picOriginName": "图片的原始名字", "picBase64": ls_f.decode('utf-8'), "nms": "0.6", "score": "0.3", "modelTpyes":"image/jpeg"}))
        print(res.text)
        time_use = time.time() - time_s
        use_time += time_use
        print(index, time_use)

    print(use_time)
    print(index, time.time() - time_start)

