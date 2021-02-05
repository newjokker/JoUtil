# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import shapely
from shapely.geometry import Polygon
import numpy as np

# todo 只是适用于凸多边形

poly1_points = [[0,0], [10,0], [12,6], [2,6]]
poly1 = Polygon(poly1_points).convex_hull          # 凸多边形

poly2_points = [[5,3], [15,3], [17,9], [7,9]]
poly2 = Polygon(poly2_points).convex_hull          # 凸多边形





print(poly1.area)
poly3 = poly1.union(poly2)

# poly3 = poly1.intersection(poly2)

print(poly3.area)


