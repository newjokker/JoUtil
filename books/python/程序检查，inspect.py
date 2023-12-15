# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import inspect
from functools import wraps


def A(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        msg_list = inspect.stack()
        for msg in msg_list:
            print(msg.function, msg.lineno, msg.filename, msg.code_context)
        result = func(*args, **kwargs)
        return result
    return wrapper

class test:
    __slots__ = (
        "a",
        "b"
    )

    def __init__(self, x, y):
        self.a = x
        self.b = y
@A
def B():
    print("OK_B")

def D():
    C()

def C():
    B()


if __name__ == "__main__":
    print(test.__dict__)
    D()




