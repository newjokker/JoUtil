# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from aip import AipFace
import base64
import time
import os
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes

""" 你的 APPID AK SK """

APP_ID = '20545883'
API_KEY = 'H9zVmG4XH9W9aMRRnQxlIQaH'
SECRET_KEY = 'oR1VGlzRCGtGgGfDCekOGs2pjKIdep28'

# APP_ID = '27684575'
# API_KEY = 'DGmI0Qagz2So8V8UcZpU6lao'
# SECRET_KEY = 'yPQtGAfWF1AUzjlmA4DozTHh5K69YUDa'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)


save_dir = r"C:\Users\14271\Desktop\heello\output_dir"
img_dir = r"C:\Users\14271\Desktop\heello\input_dir"

def dete_face(img_path):
    """检测一张图片中的人脸"""
    with open(img_path, "rb") as f:
        data = f.read()
        encodestr = base64.b64encode(data) # 得到 byte 编码的数据
        image = str(encodestr,'utf-8')

    imageType = "BASE64"
    """ 如果有可选参数 """
    # options = {"face_field": "glass", "max_face_num": 10, "face_type": "LIVE", "liveness_control": "LOW"}
    options = {"face_field": "glass"}
    # options["min_face_num"] = 2
    """ 带参数调用人脸检测 """
    res = client.detect(image, imageType, options)

    # face_info = []
    # if 'result' in res:
    #     if not res["result"]:
    #         return face_info
    # else:
    #     return face_info
    #
    # # itoration
    # face_num = res['result']['face_num']
    # for i in range(face_num):
    #     loc = res['result']['face_list'][i]['location']
    #     x1, y1 = loc['left'], loc['top']
    #     width, height = loc['width'], loc['height']
    #     x2, y2 = x1 + width, y1 + height
    #     face_info.append([int(x1), int(y1), int(x2), int(y2)])

    print(res["result"]["face_list"][0]['face_probability'])

    # return face_info

# OperateDeteRes.crop_imgs(img_dir, xml_dir=img_dir, save_dir=save_dir)


# todo 测试正脸的图片


for img_path in FileOperationUtil.re_all_file(img_dir, lambda x:str(x).endswith(('.JPG', '.jpg', '.png', '.PNG'))):
    dete_res = DeteRes(assign_img_path=img_path)
    res = dete_face(img_path)
    print(res)
    for index, each_res in enumerate(res):
        x1, y1, x2, y2 = each_res
        dete_res.add_obj(x1=x1, y1=y1, x2=x2, y2=y2, tag='face', assign_id=index)
    save_path = os.path.join(save_dir, os.path.split(img_path)[1])
    dete_res.draw_dete_res(save_path)

    time.sleep(3)





