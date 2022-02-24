# -*- coding: utf-8  -*-
# -*- author: jokker -*-


"""
__cmp__ 是所有比较魔法方法中最基础的一个，它实际上定义了所有比较操作符的行为（<,==,!=,等等），
但是它可能不能按照你需要的方式工作（例如，判断一个实例和另一个实例是否相等采用一套标准，而与判断一个实例是否大于另一实例采用另一套）。
__cmp__ 应该在 self < other 时返回一个负整数，在 self == other 时返回0，在 self > other 时返回正整数。
最好只定义你所需要的比较形式，而不是一次定义全部。 如果你需要实现所有的比较形式，而且它们的判断标准类似，
那么 __cmp__ 是一个很好的方法，可以减少代码重复，让代码更简洁。
"""


class Word(str):
    """单词类，按照单词长度来定义比较行为"""

    def __new__(cls, word):
        # 注意，我们只能使用 __new__ ，因为str是不可变类型
        # 所以我们必须提前初始化它（在实例创建时）
        if ' ' in word:
            print("Value contains spaces. Truncating to first space.")
            word = word[:word.index(' ')]
            # Word现在包含第一个空格前的所有字母
        return str.__new__(cls, word)

    def __eq__(self, other):
        return len(self) == len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __le__(self, other):
        return len(self) <= len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ne__(self, other):
        return len(self) != len(other)



if __name__ == "__main__":

    a = Word('jokker')
    b = Word("lisa")

    print("a > b : {0}".format(a > b))
    print("a >= b : {0}".format(a >= b))
    print("a < b : {0}".format(a < b))
    print("a <= b : {0}".format(a <= b))
    print("a == b : {0}".format(a == b))
    print("a != b : {0}".format(a != b))











