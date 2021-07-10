# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from JoTools.txkj.imageAugmentation import ImageAugmentation
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.operateDeteRes import OperateDeteRes, OperateTrainData

img_dir = r"/home/ldq/001_train_data/fzc_step_1_5_20210601/origin"

OperateTrainData.augmente_classify_img(img_dir, expect_img_num=15000)

