# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.utils.FileOperationUtil import FileOperationUtil
import requests
import json

img_dir = r"C:\Users\14271\Desktop\del"
url = 'http://192.168.3.221:11123/save'
# url = 'http://172.17.0.3:11123/save'
save_txt_path = r"./res.txt"

with open(save_txt_path, 'w') as txt_file:
    for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg', '.png']):
        files = {'image': open(each_img_path, 'rb')}
        res = requests.post(url=url, files=files, data={})
        print(res.text.strip())
        res_info = json.loads(res.text.strip())
        if res_info['status'] == 'success':
            txt_file.write(f'{res_info["url"]}\n')




