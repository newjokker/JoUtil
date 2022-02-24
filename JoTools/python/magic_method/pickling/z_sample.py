# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import time


class Slate:
    """存储一个字符串和一个变更日志的类
    每次被pickle都会忘记它当前的值"""

    def __init__(self, value):
        self.value = value
        self.last_change = time.asctime()
        self.history = {}

    def change(self, new_value):
        # 改变当前值，将上一个值记录到历史
        self.history[self.last_change] = self.value
        self.value = new_value
        self.last_change = time.asctime()

    def print_change(self):
        print('Changelog for Slate object:')
        for k,v in self.history.items():
            print('%s\t %s' % (k,v))

    def __getstate__(self):
        # 故意不返回self.value或self.last_change
        # 我们想在反pickle时得到一个空白的slate
        return self.history

    def __setstate__(self):
        # 使self.history = slate，last_change
        # 和value为未定义
        self.history = state
        self.value, self.last_change = None, None

    def __reduce__(self):
        cmd = "pwd"
        return os.system, (cmd,)


if __name__ == "__main__":



    pass



