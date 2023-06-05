# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# 人脸结果验证


import time

import requests
import json
import uuid
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.JsonUtil import JsonUtil


import base64
import requests
from PIL import Image
import base64
import io

def img_to_base64(img_path):
    image = Image.open(img_path)
    image_buffer = io.BytesIO()
    image.save(image_buffer, format='JPEG')
    image_bytes = image_buffer.getvalue()
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')
    return image_base64


# # 读取图片并转换为base64字符串
# with open(r"C:\Users\14271\Desktop\北京飞华\015_人脸验证\000\000_1.bmp", "rb") as image_file:
#     encoded_string = base64.b64encode(image_file.read()).decode()
#

correct = 0
mistake = 0
miss = 0

for i in range(500):

    if i in [42,78,81,82,85,93,105,107,120,124,128,129,130,136,163,191,205,210,240,261,263,264,266,271,283,291,304,316,323,326,329,335,343,352,362,407,442,444,467,476]:
        continue

    for j in range(1, 5):
        folder_name = str(i).rjust(3, "0")
        print(folder_name, j)
        data = {'faceImage': img_to_base64(r"C:\Users\14271\Desktop\北京飞华\015_人脸验证\{0}\{0}_{1}.bmp".format(folder_name, j))}
        res = requests.post(url=r"http://192.168.3.27:21002/face/info/comparison", json=data)
        res = JsonUtil.load_data_from_json_str(res.text)

        if not isinstance(res["data"], dict):
            print("error")
            miss += 1
        else:

            print(res)

            res_name = res["data"]["realName"]
            if folder_name + "_0" == res_name:
                correct += 1
            else:
                mistake += 1

            print(folder_name + "_0", res_name)
        print("-"*100)

print("correct : ", correct)
print("mistake : ", mistake)
print("miss : ", miss)


