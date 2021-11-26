# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import fileinput


with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')

