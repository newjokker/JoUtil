# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.utils.FileOperationUtil import FileOperationUtil
import requests
import json


# img_dir_list = list(FileOperationUtil.re_all_folder(r"\\192.168.3.80\算法-数据交互\输电调试图 debug del 20220710\输电缺陷按类forDebug", recurse=False))
img_dir_list = [r"C:\Users\14271\Desktop\红外缺陷检测"]


for img_dir in img_dir_list:
    save_txt_path = os.path.join(r"C:\Users\14271\Desktop", os.path.split(img_dir)[1] + '.txt')
    # url = 'http://192.168.3.221:11123/save'
    url = 'http://192.168.3.221:8000/save'
    # url = 'http://192.168.4.175:8000/save'

    with open(save_txt_path, 'w') as txt_file:
        for each_img_path in list(FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg', '.png', '.JPG', '.PNG'])):
            files = {'image': open(each_img_path, 'rb')}
            res = requests.post(url=url, files=files, data={"test": "haha", "name": FileOperationUtil.bang_path(each_img_path)[1]})
            # print(res.text.strip())
            # print(each_img_path)
            res_info = json.loads(res.text.strip())
            if res_info['status'] == 'success':
                print(f"urls : ", res_info["url"])
                txt_file.write(f'{res_info["url"]}\n')




