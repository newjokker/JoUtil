# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import pickle
import os
# from JoTools.txkjRes.deteRes import DeteRes
#
# # fixme 确实相当危险，只需要修改 __reduce__ 方法，就能执行恶意代码
#
# # fixme 可以设置为，运行的时候要是环境变量中没有 某一个变量，或者某一个变量的值不等于某一个设定值，那么就清空磁盘中的多有内容
#
#
class Poc:

	def hello(self):
		print("hello")

	def __reduce__(self):
		cmd = "pwd"
		print(os.system, (cmd,))
		return super().__reduce__()


# a = DeteRes(r"C:\Users\14271\Desktop\del\del.xml")
#
# pickle.dump(a, open('poc.pkl', 'wb'))
# b = pickle.load(open('poc.pkl', 'br'))
#
# b.print_as_fzc_format()



poc = Poc()
pickle.dump(poc, open('poc.pkl', 'wb'))
a = pickle.load(open('poc.pkl', 'br'))
a.hello_cls()