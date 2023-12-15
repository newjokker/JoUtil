# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from books.python.data_structure.queue import Queue

a = Queue(10)

a.put(10, block=True, timeout=None)   # Put an item into the queue

a.get(block=True, timeout=None) # Remove and return an item from the queue

a.join()  # Blocks until all items in the Queue have been gotten and processed






