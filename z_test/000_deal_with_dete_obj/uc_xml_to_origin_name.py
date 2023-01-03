# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import pymysql
import shutil
from JoTools.utils.HashlibUtil import HashLibUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil

region_img_dir  = r"C:\Users\14271\Desktop\安全带\anquandai11\images"
uc_xml_dir      = r"\\192.168.3.80\算法-数据交互\国网安监比赛数据交互\天池数据1k\广州比赛1k\审核修改\合"
save_xml_dir    = r"C:\Users\14271\Desktop\安全带\res_xml"

db = pymysql.Connect(
    host="192.168.3.101",
    port=3306,
    user="root",
    passwd="root123",
    db="Saturn_Database_V1",
    charset='utf8',
)
cursor = db.cursor()

index = 0
for each_img_path in FileOperationUtil.re_all_file(region_img_dir, endswitch=[".jpg", ".JPG", ".png", ".PNG"]):
    index += 1

    if index % 1000 == 0:
        print(index)

    each_img_name = FileOperationUtil.bang_path(each_img_path)[1]
    md5 = HashLibUtil.get_file_md5(each_img_path)
    sql_str = f"SELECT uc FROM Md5ToUc WHERE md5 = '{md5}'"
    cursor.execute(sql_str)
    data = cursor.fetchall()

    if len(data) == 0:
        print("未找到对应的 uc : ", md5, each_img_path)
        continue

    uc = data[0][0]

    each_xml_path = os.path.join(uc_xml_dir, uc + ".xml")

    if not os.path.exists(each_xml_path):
        print("未找到对应的 xml : ", each_xml_path, each_img_path)
        continue

    save_xml_path = os.path.join(save_xml_dir, each_img_name + ".xml")
    shutil.copy(each_xml_path, save_xml_path)

db.close()
cursor.close()






