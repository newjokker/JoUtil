# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import time
from threading import Thread


def countdown(n):
    while n >0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)



if __name__ == "__main__":

    t1 = Thread(target=countdown, args=(5, ))
    t2 = Thread(target=countdown, args=(25, ))
    t1.start()
    t2.start()

    t1.join(timeout=2)       # 用于阻塞主进程运行的，只有当 t1 运行完了主进程才能运行, timeout 设置阻塞的最长时间
    # t2.join()

    for i in range(100, 200, 10):
        print(i**2)
        time.sleep(1)






