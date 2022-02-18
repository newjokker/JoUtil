# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# fixme 代码跑分

import os
import pylint
import subprocess


a = pylint.checkers.BaseChecker()




each_std_file = open(r"C:\Users\14271\Desktop\del.txt", 'w')

subprocess.Popen(r"pylint simple D:\Algo\jo_util\JoTools\txkjRes\deteRes.py", stdout=each_std_file, shell=False)


class CheckCodeStyleByPEP8(object):
    """使用 pep8 规范检查代码"""
    pass


"""
F（ 致命错误）。
C（error，错误）：很可能是代码中的错误。
W（warning，警告）：某些 Python 特定的问题。
R（refactor，重构）：写得非常糟糕的代码。
C（convention，规范）：违反编码风格标准 。
"""