# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from towhee import pipe

add_one = (
    pipe.input('x')
        .map('x', 'y', lambda x: x + 1)
        .map('y', 'z', lambda x: x**2 + 1)
        .output('z')
)

res = add_one(1).get()

print(res)

