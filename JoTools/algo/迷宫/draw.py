# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import numpy as np

import random
from matplotlib import pyplot as plt


def build_twist(num_rows, num_cols):  # 扭曲迷宫
	# (行坐标，列坐标，四面墙的有无&访问标记)
    m = np.zeros((num_rows, num_cols, 5), dtype=np.uint8)
    r, c = 0, 0
    trace = [(r, c)]
    while trace:
        r, c = random.choice(trace)
        m[r, c, 4] = 1	# 标记为通路
        trace.remove((r, c))
        check = []
        if c > 0:
            if m[r, c - 1, 4] == 1:
                check.append('L')
            elif m[r, c - 1, 4] == 0:
                trace.append((r, c - 1))
                m[r, c - 1, 4] = 2	# 标记为已访问
        if r > 0:
            if m[r - 1, c, 4] == 1:
                check.append('U')
            elif m[r - 1, c, 4] == 0:
                trace.append((r - 1, c))
                m[r - 1, c, 4] = 2
        if c < num_cols - 1:
            if m[r, c + 1, 4] == 1:
                check.append('R')
            elif m[r, c + 1, 4] == 0:
                trace.append((r, c + 1))
                m[r, c + 1, 4] = 2
        if r < num_rows - 1:
            if m[r + 1, c, 4] == 1:
                check.append('D')
            elif m[r + 1, c, 4] == 0:
                trace.append((r + 1, c))
                m[r + 1, c, 4] = 2
        if len(check):
            direction = random.choice(check)
            if direction == 'L':	# 打通一面墙
                m[r, c, 0] = 1
                c = c - 1
                m[r, c, 2] = 1
            if direction == 'U':
                m[r, c, 1] = 1
                r = r - 1
                m[r, c, 3] = 1
            if direction == 'R':
                m[r, c, 2] = 1
                c = c + 1
                m[r, c, 0] = 1
            if direction == 'D':
                m[r, c, 3] = 1
                r = r + 1
                m[r, c, 1] = 1
    m[0, 0, 0] = 1
    m[num_rows - 1, num_cols - 1, 2] = 1
    return m

def draw(num_rows, num_cols, m):
    image = np.zeros((num_rows * 10, num_cols * 10), dtype=np.uint8)
    for row in range(0, num_rows):
        for col in range(0, num_cols):
            cell_data = m[row, col]
            for i in range(10 * row + 2, 10 * row + 8):
                image[i, range(10 * col + 2, 10 * col + 8)] = 255
            if cell_data[0] == 1:
                image[range(10 * row + 2, 10 * row + 8), 10 * col] = 255
                image[range(10 * row + 2, 10 * row + 8), 10 * col + 1] = 255
            if cell_data[1] == 1:
                image[10 * row, range(10 * col + 2, 10 * col + 8)] = 255
                image[10 * row + 1, range(10 * col + 2, 10 * col + 8)] = 255
            if cell_data[2] == 1:
                image[range(10 * row + 2, 10 * row + 8), 10 * col + 9] = 255
                image[range(10 * row + 2, 10 * row + 8), 10 * col + 8] = 255
            if cell_data[3] == 1:
                image[10 * row + 9, range(10 * col + 2, 10 * col + 8)] = 255
                image[10 * row + 8, range(10 * col + 2, 10 * col + 8)] = 255
    return image

def draw_path(image, move_list):
    row, col = (0, 0)
    image[range(10 * row + 2, 10 * row + 8), 10 * col] = 127
    image[range(10 * row + 2, 10 * row + 8), 10 * col + 1] = 127
    for i in range(len(move_list) + 1):
        for x in range(10 * row + 2, 10 * row + 8):
            image[x, range(10 * col + 2, 10 * col + 8)] = 127
        if i > 0:
            go = move_list[i - 1]
            if go == 'L':
                image[range(10 * row + 2, 10 * row + 8), 10 * col + 9] = 127
                image[range(10 * row + 2, 10 * row + 8), 10 * col + 8] = 127
            elif go == 'U':
                image[10 * row + 9, range(10 * col + 2, 10 * col + 8)] = 127
                image[10 * row + 8, range(10 * col + 2, 10 * col + 8)] = 127
            elif go == 'R':
                image[range(10 * row + 2, 10 * row + 8), 10 * col] = 127
                image[range(10 * row + 2, 10 * row + 8), 10 * col + 1] = 127
            elif go == 'D':
                image[10 * row, range(10 * col + 2, 10 * col + 8)] = 127
                image[10 * row + 1, range(10 * col + 2, 10 * col + 8)] = 127
        if i >= len(move_list):
            break
        go = move_list[i]
        if go == 'L':
            image[range(10 * row + 2, 10 * row + 8), 10 * col] = 127
            image[range(10 * row + 2, 10 * row + 8), 10 * col + 1] = 127
        elif go == 'U':
            image[10 * row, range(10 * col + 2, 10 * col + 8)] = 127
            image[10 * row + 1, range(10 * col + 2, 10 * col + 8)] = 127
        elif go == 'R':
            image[range(10 * row + 2, 10 * row + 8), 10 * col + 9] = 127
            image[range(10 * row + 2, 10 * row + 8), 10 * col + 8] = 127
        elif go == 'D':
            image[10 * row + 9, range(10 * col + 2, 10 * col + 8)] = 127
            image[10 * row + 8, range(10 * col + 2, 10 * col + 8)] = 127
        if go == 'L':
            col = col - 1
        elif go == 'U':
            row = row - 1
        elif go == 'R':
            col = col + 1
        elif go == 'D':
            row = row + 1
    image[range(10 * row + 2, 10 * row + 8), 10 * col + 9] = 127
    image[range(10 * row + 2, 10 * row + 8), 10 * col + 8] = 127
    return image

def solve_fill(num_rows, num_cols, m):  # 填坑法
    map_arr = m.copy()	# 拷贝一份迷宫来填坑
    map_arr[0, 0, 0] = 0
    map_arr[num_rows-1, num_cols-1, 2] = 0
    move_list = []
    xy_list = []
    r, c = (0, 0)
    while True:
        if (r == num_rows-1) and (c == num_cols-1):
            break
        xy_list.append((r, c))
        wall = map_arr[r, c]
        way = []
        if wall[0] == 1:
            way.append('L')
        if wall[1] == 1:
            way.append('U')
        if wall[2] == 1:
            way.append('R')
        if wall[3] == 1:
            way.append('D')
        if len(way) == 0:
            return False
        elif len(way) == 1:	# 在坑中
            go = way[0]
            move_list.append(go)
            if go == 'L':	# 填坑
                map_arr[r, c, 0] = 0
                c = c - 1
                map_arr[r, c, 2] = 0
            elif go == 'U':
                map_arr[r, c, 1] = 0
                r = r - 1
                map_arr[r, c, 3] = 0
            elif go == 'R':
                map_arr[r, c, 2] = 0
                c = c + 1
                map_arr[r, c, 0] = 0
            elif go == 'D':
                map_arr[r, c, 3] = 0
                r = r + 1
                map_arr[r, c, 1] = 0
        else:
            if len(move_list) != 0:	# 不在坑中
                come = move_list[len(move_list)-1]
                if come == 'L':
                    if 'R' in way:
                        way.remove('R')
                elif come == 'U':
                    if 'D' in way:
                        way.remove('D')
                elif come == 'R':
                    if 'L' in way:
                        way.remove('L')
                elif come == 'D':
                    if 'U' in way:
                        way.remove('U')
            go = random.choice(way)	# 随机选一个方向走
            move_list.append(go)
            if go == 'L':
                c = c - 1
            elif go == 'U':
                r = r - 1
            elif go == 'R':
                c = c + 1
            elif go == 'D':
                r = r + 1
    r_list = xy_list.copy()
    r_list.reverse()	# 行动坐标记录的反转
    i = 0
    while i < len(xy_list)-1:	# 去掉重复的移动步骤
        j = (len(xy_list)-1) - r_list.index(xy_list[i])
        if i != j:	# 说明这两个坐标之间的行动步骤都是多余的，因为一顿移动回到了原坐标
            del xy_list[i:j]
            del move_list[i:j]
            r_list = xy_list.copy()
            r_list.reverse()
        i = i + 1
    return move_list

def solve_backtrack(num_rows, num_cols, map_arr):  # 回溯法
    move_list = ['R']
    m = 1	# 回溯点组号
    mark = []
    r, c = (0, 0)
    while True:
        if (r == num_rows-1) and (c == num_cols-1):
            break
        wall = map_arr[r, c]
        way = []
        if wall[0] == 1:
            way.append('L')
        if wall[1] == 1:
            way.append('U')
        if wall[2] == 1:
            way.append('R')
        if wall[3] == 1:
            way.append('D')
        come = move_list[len(move_list) - 1]
        if come == 'L':
            way.remove('R')
        elif come == 'U':
            way.remove('D')
        elif come == 'R':
            way.remove('L')
        elif come == 'D':
            way.remove('U')
        while way:
            mark.append((r, c, m, way.pop()))	# 记录当前坐标和可行移动方向
        if mark:
            r, c, m, go = mark.pop()
            del move_list[m:]	# 删除回溯点之后的移动
        else:
            return False
        m = m + 1
        move_list.append(go)
        if go == 'L':
            c = c - 1
        elif go == 'U':
            r = r - 1
        elif go == 'R':
            c = c + 1
        elif go == 'D':
            r = r + 1
    del move_list[0]
    return move_list


rows = 30
cols = 30

Map = build_twist(rows, cols)

print(Map.shape)

exit()


plt.imshow(draw(rows, cols, Map), cmap='gray')

fig = plt.gcf()
fig.set_size_inches(cols/10/3, rows/10/3)
plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.gca().yaxis.set_major_locator(plt.NullLocator())
plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
plt.margins(0, 0)
fig.savefig('aaa.png', format='png', transparent=True, dpi=300, pad_inches=0)

move = solve_backtrack(rows, cols, Map)
plt.imshow(draw_path(draw(rows, cols, Map), move), cmap='hot')
fig = plt.gcf()
fig.set_size_inches(cols/10/3, rows/10/3)
plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.gca().yaxis.set_major_locator(plt.NullLocator())
plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
plt.margins(0, 0)
fig.savefig('bbb.png', format='png', transparent=True, dpi=300, pad_inches=0)
