# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# refer : https://blog.csdn.net/qq_40187062/article/details/108929405

class NewDict(dict):


    def __missing__(self, key):
        print(f'__missing__被调用')
        return 1000

    def __getitem__(self, item):
        print(f'__getitem__被调用')
        ret = super(NewDict, self).__getitem__(item)
        return ret


if __name__ == "__main__":

    nd = NewDict(a=1, b=2)
    print(nd['a'])





