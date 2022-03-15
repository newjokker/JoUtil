# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import numpy as np
import matplotlib.pyplot as plt


# 核心代码，求斜率w,截距b
def fit(points):
    data_x, data_y = zip(*points)
    m = len(data_y)
    x_bar = np.mean(data_x)
    sum_yx = 0
    sum_x2 = 0
    sum_delta = 0
    for i in range(m):
        x = data_x[i]
        y = data_y[i]
        sum_yx += y * (x - x_bar)
        sum_x2 += x ** 2
    # 根据公式计算w
    w = sum_yx / (sum_x2 - m * (x_bar ** 2))
    for i in range(m):
        x = data_x[i]
        y = data_y[i]
        sum_delta += (y - w * x)
    b = sum_delta / m
    return w, b


points = np.array([(1,1), (2,2), (5,5), (7,8)])
x, y = zip(*points)
x = np.array(x)
y = np.array(y)
# 计算并绘制
w, b = fit(points)


x_min = min(x)
x_max = max(x)

pred_y = [w * x_min + b, w * x_max + b]
plt.scatter(x, y)
plt.plot([x_min, x_max], pred_y, c='r', label='line')
plt.show()