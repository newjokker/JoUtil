# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from collections import Counter


a = {'a':1, 'b':2, 'c':3}
b = {'b':1, 'c':2, 'e':3}

c = Counter(a) + Counter(b)
# c = Counter(a) - Counter(b)


print(c.most_common(1))

print(c)



