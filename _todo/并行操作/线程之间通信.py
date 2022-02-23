# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import time
from queue import Queue
from threading import Thread


def producer(out_q):
    while True:
        data = time.time()
        out_q.put(data)
        time.sleep(0.5)

def consumer(in_q):
    while True:
        print(q.full())
        data = in_q.get()
        print(data)
        time.sleep(1)


if __name__ == "__main__":

    # 传入队列实现线程之间的通信
    # Queue 实例已经拥有了所有所需要的锁，因此他们可以安全地在任意多的线程之间共享
    q = Queue(20)

    t1 = Thread(target=producer, args=(q, ))
    t2 = Thread(target=consumer, args=(q, ))

    t1.start()
    t2.start()




