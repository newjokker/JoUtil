
import numpy as np
from JoTools.utils.DecoratorUtil import DecoratorUtil

import math


def find_short_edges(points):
    edges = []
    for i in range(4):
        for j in range(i + 1, 4):
            edges.append((points[i], points[j]))

    # 计算每条边的长度
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    lengths = [distance(edge[0], edge[1]) for edge in edges]

    # 找到最短边
    short_edges = sorted(edges, key=lambda e: distance(e[0], e[1]))[:2]

    # 计算短边中点
    mid_points = [(int((edge[0][0] + edge[1][0]) / 2), int((edge[0][1] + edge[1][1]) / 2)) for edge in short_edges]

    # 短边端点
    endpoints = [edge[0] for edge in short_edges] + [edge[1] for edge in short_edges]

    return mid_points, endpoints


def euclidean_distance(rectangle1, rectangle2):
    mid_points1, endpoints1 = find_short_edges(rectangle1)
    mid_points2, endpoints2 = find_short_edges(rectangle2)

    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    min_dist = float('inf')
    for mid_point in mid_points1:
        for endpoint in endpoints2:
            dist = distance(mid_point, endpoint)
            if dist < min_dist:
                min_dist = dist

    for mid_point in mid_points2:
        for endpoint in endpoints1:
            dist = distance(mid_point, endpoint)
            if dist < min_dist:
                min_dist = dist

    return min_dist


# def euclidean_distance(p1, p2):
#     """ 计算两点之间的欧几里得距离 """
#     # return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
#     return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) + (abs(p1[2])*0 - abs(p2[2])*0)**2
#

@DecoratorUtil.time_this
def point_algo(points):
    """ 使用最近邻贪心算法对点进行排序 """
    n = len(points)
    if n <= 1:
        return points

    # 从第一个点开始
    path = [points[0]]
    remaining_points = points[1:]

    while remaining_points:
        last_point = path[-1]
        next_point, min_dist = min(
            ((point, euclidean_distance(last_point, point)) for point in remaining_points),
            key=lambda x: x[1]
        )
        path.append(next_point)
        remaining_points.remove(next_point)

    return path
