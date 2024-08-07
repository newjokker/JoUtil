import matplotlib.pyplot as plt
from JoTools.utils.DecoratorUtil import DecoratorUtil
from algo import point_algo
import random

@DecoratorUtil.time_this
def load_point(data_path):
    def read_text_dat(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()
        return data
    text_data = read_text_dat(data_path)
    coordinates = eval(text_data)
    return coordinates


import numpy as np
import math

def load_point2(data_path):
    def read_text_dat(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()
        return data
    def get_center_point(each_point):
        x1, y1 = each_point[0]
        x2, y2 = each_point[1]
        x3, y3 = each_point[2]
        x4, y4 = each_point[3]
        return  [(y1+y2+y3+y4)/4, (x1+x2+x3+x4)/4]
    text_data = read_text_dat(data_path)
    points = []
    for each in text_data.split("\n"):
        each_point = eval(f"[{each}]")
        points.append(each_point)
    return points


def calculate_long_side_midpoints_and_draw(rectangles):
    # fig, ax = plt.subplots()
    fig, ax = plt.subplots(figsize=(20, 20))

    for points in rectangles:
        A, B, C, D = points

        # 计算边的长度
        AB = np.linalg.norm(np.array(B) - np.array(A))
        BC = np.linalg.norm(np.array(C) - np.array(B))
        CD = np.linalg.norm(np.array(D) - np.array(C))
        DA = np.linalg.norm(np.array(A) - np.array(D))

        # 确定短边
        short_sides = sorted([(AB, A, B), (BC, B, C), (CD, C, D), (DA, D, A)])[:2]

        center = ((A[0] + C[0]) / 2, (A[1] + C[1]) / 2)

        # 计算短边中点
        midpoints = []
        for _, point1, point2 in short_sides:
            midpoint = (np.array(point1) + np.array(point2)) / 2
            midpoints.append(midpoint)

        # # 绘制矩形
        # ax.plot(*zip(*points), 'o-', label='Rectangle')  # 绘制矩形

        ax.plot(center[0], center[1], 'go', color='black', markersize=10)

        # 绘制中点
        ax.plot(*zip(*midpoints), 'ro', label='Midpoints')  # 绘制中点

        # 绘制连线
        ax.plot(*zip(*midpoints), 'r--', label='Midpoint Line')  # 绘制连线

    real_point = get_point_from_rect(rectangles)
    lats = [lat for lat, lon in real_point]
    lons = [lon for lat, lon in real_point]
    # fig, ax = plt.subplots(figsize=(20,20))
    ax.set_title('Points on the Map')
    # 绘制线条
    ax.plot(lons, lats, marker='o', linestyle='', color='red', markersize=6, label='Points')

    ax.plot(lons, lats, linestyle='-', color='blue', label='Path')
    ax.set_aspect('equal', adjustable='datalim')

    # 设置图表标题和坐标轴标签
    ax.set_title('Rectangles and Long Side Midpoint Lines')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')

    # # 添加图例
    # ax.legend()

    # 显示图表
    plt.show()


@DecoratorUtil.time_this
# def plot_points(coordinates):
#     lats = [lat for lat, lon in coordinates]
#     lons = [lon for lat, lon in coordinates]
#     # fig, ax = plt.subplots(figsize=(20,20))
#     ax.set_title('Points on the Map')
#     # 绘制线条
#     ax.plot(lons, lats, marker='o', linestyle='', color='red', markersize=6, label='Points')
#
#     ax.plot(lons, lats, linestyle='-', color='blue', label='Path')
#     ax.set_aspect('equal', adjustable='datalim')
#
#     # 显示图形
#     plt.show()


def get_point_from_rect(rects):
    points = []
    for each_rect in rects:
        A,B,C,D = each_rect
        points.append(((A[1]+B[1]+C[1]+D[1])/4, (A[0]+B[0]+C[0]+D[0])/4))
    return points


if __name__ == "__main__":


    # points = load_point(r"./data/demo_data3.dat")
    points = load_point2(r"./data/g11_geo.dat")
    #
    random.shuffle(points)

    points = point_algo(points)

    real_point = get_point_from_rect(points)

    calculate_long_side_midpoints_and_draw(points)
