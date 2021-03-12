# -*- coding: utf-8  -*-
# -*- author: jokker -*-



from multiprocessing import Pool
from functools import partial
import random
import time


def somefunc(str_1, str_2, iterable_iterm):
    time.sleep(random.randint(3,3))
    print("%s %s %d" % (str_1, str_2, iterable_iterm))

def main():
    iterable = [1, 2, 3, 4, 5]
    pool = Pool()
    str_1 = "This"
    str_2 = "is"
    func = partial(somefunc, str_1, str_2)
    pool.map(func, iterable)
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
