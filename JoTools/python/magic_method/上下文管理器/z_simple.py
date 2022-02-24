# -*- coding: utf-8  -*-
# -*- author: jokker -*-



class Closer:
    """一个上下文管理器，可以在with语句中使用close()自动关闭对象"""

    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return str(self.obj) # 绑定到目标

    def __exit__(self, exception_type, exception_value, traceback):
        try:
            self.obj.close()
        except AttributeError: # obj不是可关闭的
            print('Not closable.')
            return True # 成功地处理了异常


if __name__ == "__main__":


    with Closer(r"123.txt") as test:
        print(test, len(test))




