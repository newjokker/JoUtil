# -*- coding: utf-8  -*-
# -*- author: jokker -*-

"""
数据结构堆（heap）是一种优先队列。 使用优先队列能够以任意顺序增加对象，并且能在任意的时间（可能在增加对象的同时）找到（也可能移除）最小的元素，
也就是说它比python的min方法更加有效率。 heapify 函数将使用任意列表作为参数，并且尽可能少的移位操作，将其转化为合法的堆
"""


import heapq



H = [21,1,45,78,3,5]
# Use heapify to rearrange the elements
heapq.heapify(H)        #
print(H)


heapq.heappush(H,8)     # push
print(H)

heapq.heappop(H)        # pop
print(H)


# heapreplace函数总是删除堆的最小元素，并将新的传入元素插入到任何未被任何顺序修复的位置。
heapq.heapreplace(H,6)
print(H)


