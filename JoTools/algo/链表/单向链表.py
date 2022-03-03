# -*- coding: utf-8  -*-
# -*- author: jokker -*-


class Node(object):
    """单链表的结点"""
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList(object):
    """单链表"""

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def items(self):
        cur = self._head
        while cur is not None:
            yield cur.item
            cur = cur.next

    def add(self, item):
        node = Node(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, index, item):
        if index <= 0:
            self.add(item)
        elif index > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            for i in range(index - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        cur = self._head
        pre = None
        while cur is not None:
            if cur.item == item:
                if not pre:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                return True
            else:
                pre = cur
                cur = cur.next

    def find(self, item):
        return item in self.items()



if __name__ == "__main__":


    link_list = SingleLinkList()
    # 向链表尾部添加数据
    for i in range(5):
        link_list.append(i)

    # 链表数据插入数据
    link_list.insert(3, 9)

    print(list(link_list.items()))
