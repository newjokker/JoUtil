# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from aip import AipFace
import base64
import cv2
import os
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes


""" 你的 APPID AK SK """

APP_ID = '20545883'
API_KEY = 'H9zVmG4XH9W9aMRRnQxlIQaH'
SECRET_KEY = 'oR1VGlzRCGtGgGfDCekOGs2pjKIdep28'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)


save_dir = r"C:\Users\14271\Desktop\人脸识别\human_face"
img_dir = r"C:\Users\14271\Desktop\人脸识别\region_img"

def dete_face(img_path):
    """检测一张图片中的人脸"""
    with open(img_path, "rb") as f:
        data = f.read()
        encodestr = base64.b64encode(data) # 得到 byte 编码的数据
        image = str(encodestr,'utf-8')

    imageType = "BASE64"
    """ 如果有可选参数 """
    options = {"face_field": "age", "max_face_num": 10, "face_type": "LIVE", "liveness_control": "LOW"}
    # options["min_face_num"] = 2
    """ 带参数调用人脸检测 """
    res = client.detect(image, imageType, options)

    face_info = []
    if not res["result"]:
        return face_info

    # itoration
    face_num = res['result']['face_num']
    for i in range(face_num):
        loc = res['result']['face_list'][i]['location']
        x1, y1 = loc['left'], loc['top']
        width, height = loc['width'], loc['height']
        x2, y2 = x1 + width, y1 + height
        face_info.append([int(x1), int(y1), int(x2), int(y2)])

    return face_info


for img_path in FileOperationUtil.re_all_file(img_dir, lambda x:str(x).endswith('.JPG')):
    dete_res = DeteRes(assign_img_path=img_path)
    res = dete_face(img_path)
    print(res)
    for index, each_res in enumerate(res):
        x1, y1, x2, y2 = each_res
        dete_res.add_obj(x1=x1, y1=y1, x2=x2, y2=y2, tag='face', assign_id=index)
    save_path = os.path.join(save_dir, os.path.split(img_path)[1])
    dete_res.draw_dete_res(save_path)




# # ----------------------------------------------------------------------------------------------------------------------
#
# for img_path in FileOperationUtil.re_all_file(r"C:\Users\14271\Desktop\inputImg"):
#
#     with open(img_path, "rb") as f:
#         data = f.read()
#         encodestr = base64.b64encode(data) # 得到 byte 编码的数据
#         image = str(encodestr,'utf-8')
#     # ----------------------------------------------------------------------------------------------------------------------
#
#     imageType = "BASE64"
#     """ 如果有可选参数 """
#     options = {"face_field": "age", "max_face_num": 10, "face_type": "LIVE", "liveness_control": "LOW"}
#     # options["min_face_num"] = 2
#     """ 带参数调用人脸检测 """
#     res = client.detect(image, imageType, options)
#
#     # ----------------------------------------------------------------------------------------------------------------------
#
#     print(res)
#
#     if not res['result']:
#         continue
#
#     face_num = res['result']['face_num']
#     center_list = []
#     radius = 50
#     for i in range(face_num):
#         loc = res['result']['face_list'][i]['location']
#         left, top = loc['left'], loc['top']
#         width, height = loc['width'], loc['height']
#         center = (int(left) + int(width/2), int(top) + int(height/2))
#         center_list.append(center)
#         radius = int((width + height)/2)
#
#     # ----------------------------------------------------------------------------------------------------------------------
#
#     img = cv2.imread(img_path)
#     for each_center in center_list:
#         # cv2.circle(img, each_center, 200, color=(0,0,255), thickness=5)
#         cv2.circle(img, each_center, radius, color=(0,0,255), thickness=5)
#
#     height, width = img.shape[:2]
#     # img = cv2.resize(img, (int(width / 3), int(height / 3)))
#     img = cv2.resize(img, (int(width / 1), int(height / 1)))
#     cv2.imshow('show mask', img)
#     cv2.imwrite(img_path, img)
#     # cv2.waitKey(0)
#     # cv2.destroyAllWindows()
#
# # ----------------------------------------------------------------------------------------------------------------------




