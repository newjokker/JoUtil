# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# 参考 ： https://blog.csdn.net/dcrmg/article/details/79525167


import progressbar
import time

from progressbar import *



pb = progressbar.ProgressBar(10)
pb.start()

# fixme 会报错，看一下问题所在

pb.widgets.clear()                  # 清空之前的进度条
pb.widgets.append("进度:")                # 增加标签
pb.widgets.append(Percentage())           # 进度条
pb.widgets.append(Bar('*'))               # 进度条样式
pb.widgets.append(Timer())               # 进度条样式
pb.widgets.append(" | ")               # 进度条样式
pb.widgets.append(ETA())               # 进度条样式

# pb.widgets[5] = Timer()

for i in range(10):
    time.sleep(0.1)
    pb.update(i+1)


