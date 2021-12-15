# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.deteRes import DeteRes


a = DeteRes()
b = DeteRes()

a.add_obj(1,2,3,4,'a')
a.add_obj(2,3,4,5,'b')
b.add_obj(2,3,4,5,'c')
b.add_obj(2,3,4,5,'d')

c = a + b

a.print_as_fzc_format()
print('-'*50)
b.print_as_fzc_format()
print('-'*50)

c.print_as_fzc_format()

