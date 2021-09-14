# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.utils.TxtUtil import TxtUtil
import cv2
import numpy
import numpy as np

txt_path = r"C:\Users\14271\Desktop\abstruct.txt"

a = TxtUtil.read_as_tableread_as_table(txt_path)

new_format = []

is_start = True
each_line = ""

for each in a:

    if each != ['']:
        if each[0][0] in ['0', '1','2','3','4','5','6','7','8','9']:
            is_start = True

            if is_start:
                new_format.append(''.join(each_line.split(',')[1:]))
                each_line = ""

            each_line += each[0]
        else:
            each_line += " " + each[0]
            is_start = False


for each in new_format:
    print(each)










