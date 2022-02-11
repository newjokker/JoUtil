# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.txkj.imageAugmentation import ImageAugmentation
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.operateDeteRes import OperateDeteRes, OperateTrainData

img_dir = r"C:\Users\14271\Desktop\fzc_qx"

OperateTrainData.augmente_classify_img(img_dir, expect_img_num=10000)

