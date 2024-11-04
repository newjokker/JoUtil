# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# refer : https://codeantenna.com/a/pk6wFGMqL5
# 如果for的对象没有__iter__方法，则无法获得一个迭代器，那么就会报错，但是，如果这个类实现了__getitem__方法，会从0开始依次读取相应的下标，
# 直到发生IndexError为止，str类就没有实现了_iter_方法，所以我们可以for一个str对象，让它的每一个字母都打印输出.



