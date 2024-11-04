# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import fileinput


# fixme 跑不同，不知道是什么原因

with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')

