# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import math

import numpy as np



np.load()

# p0 = [0, 0]
# p1 = [2, 0]
# p2 = [2, 1]
# p3 = [0, 1]

p0 = [1, 0]
p1 = [2, 1]
p2 = [1, 2]
p3 = [0, 1]


cx = (p0[0] + p1[0] + p2[0] + p3[0]) / 4
cy = (p0[1] + p1[1] + p2[1] + p3[1]) / 4
# cal angle
angle = math.atan(((p1[1] - p0[1]) / (p1[0] - p0[0])))  * (180 / math.pi)
# cal w h





print((p1[1] - p0[1]) ,  p1[0] - p0[0])

print(cx, cy, angle)