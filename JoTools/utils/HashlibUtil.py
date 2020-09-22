# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# 参考：https://www.liaoxuefeng.com/wiki/1016959663602400/1017686752491744

"""
* Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
* 什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。

* 摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。

* 摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。
而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。
"""

import hashlib
import os
import shutil
from ..utils.FileOperationUtil import FileOperationUtil

"""
# # 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：
"""


class HashLibUtil(object):

    @staticmethod
    def get_file_md5(file_path):
        """获取文件的 MD5 值"""
        md5 = hashlib.md5()
        with open(file_path, 'rb') as xml_file:
            md5.update(xml_file.read())
            return md5.hexdigest()

    @staticmethod
    def is_the_same_file(file_path_1, file_path_2):
        """判断两个文件是否是一个文件"""
        md5_1 = HashLibUtil.get_file_md5(file_path_1)
        md5_2 = HashLibUtil.get_file_md5(file_path_2)
        return True if md5_1 == md5_2 else False

    @staticmethod
    def duplicate_checking(file_path_list):
        """文件查重，输出重复的文件，放在一个列表里面
        DS : [[file_path_1, file_path_2], []]"""
        file_md5 = {}
        res = []
        # 计算所有文件的 md5 值
        for index, each_file_path in enumerate(file_path_list):
            print(index, each_file_path)
            md5 = HashLibUtil.get_file_md5(each_file_path)
            if md5 in file_md5:
                file_md5[md5].append(each_file_path)
            else:
                file_md5[md5] = [each_file_path]
        # 将有重复的文件放到列表中
        for each_md5 in file_md5:
            if len(file_md5[each_md5]) > 1:
                res.append(file_md5[each_md5])
        return res

    @staticmethod
    def leave_one(img_dir, save_dir=None):
        """检查路径下面有没有重复的文件，把所有不重复的文件复制到指定文件夹，或者直接在当前文件夹删除"""
        md5_set = set()
        for each_img_path in FileOperationUtil.re_all_file(img_dir, lambda x:str(x).endswith((".jpg", ".png"))):
            each_md5 = HashLibUtil.get_file_md5(each_img_path)
            if each_md5 not in md5_set:
                md5_set.add(each_md5)
                if save_dir is not None:
                    each_save_path = os.path.join(save_dir, os.path.split(each_img_path)[1])
                    shutil.copyfile(each_img_path, each_save_path)
            else:
                if save_dir is None:
                    # 不另存为文件夹，就直接在当前文件夹中将重复的图片删除
                    os.remove(each_img_path)



if __name__ == "__main__":

    # md5_str = HashLibUtil.get_file_md5(r"C:\Users\14271\Desktop\face_detection\human_face\cy\affd45ad896ddffaa1a8fdf95c5d87d0.jpg")
    # print(md5_str)
    #
    # exit()


    # filePath1 = r'C:\Users\Administrator\Desktop\for6.xml'
    # filePath2 = r'C:\Users\Administrator\Desktop\for6 - 副本.xml'
    #
    # a = HashLibUtil.is_the_same_file(filePath1, filePath2)

    # file_dir = r'C:\Users\14271\Desktop\del\深度学习\effi\food_challenge2\del'
    # file_list_1 = FileOperationUtil.re_all_file(r"C:\data\test_data\fzc\原始faster训练用的图片fzc\origin", lambda x:str(x).endswith('.jpg'))
    # file_list_2 = FileOperationUtil.re_all_file(r"C:\Users\14271\Desktop\防振锤优化\000_标准测试集\img", lambda x:str(x).endswith('.jpg'))
    # file_list = file_list_1 + file_list_2
    # dc = HashLibUtil.duplicate_checking(file_list)
    #
    # for each in dc:
    #     print(each)
    #     print("-"*100)

    HashLibUtil.leave_one(r"C:\Users\14271\Desktop\fzc报错的地方",
                          r"C:\Users\14271\Desktop\报错文件去重")



    # # fixme 删除第一个文件外的其他文件
    # import os
    # for each in dc:
    #     for i in each[1:]:
    #         print(i)
    #         os.remove(i)

