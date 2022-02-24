# -*- coding: utf-8  -*-
# -*- author: jokker -*-



class Test():

    def __init__(self, name=None, id=None):
        self.name = name
        self.id = id

    def __dir__(self):
        pass

    def __format__(self, format_spec='name-id'):
        if format_spec == "name-id":
            return "{0}-{1}".format(str(self.name), self.id)
        elif format_spec == 'id-name':
            return "{0}-{1}".format(str(self.name), self.id)

    def __hash__(self):
        return hash(str(self.name) + str(self.id))

    def __bool__(self):
        if (self.name is None) or (self.id is None):
            return False
        else:
            return True

    def __repr__(self):
        # 机器可读的输出
        return "repr:{0}-{1}".format(self.name, self.id)

    def __str__(self):
        # 人类可读的输出
        return "str:{0}-{1}".format(self.name, self.id)



if __name__ == "__main__":

    a = Test("jokker")
    print(format(a, "name-id"))

    print(hash(a))

    print(bool(a))

    print(a)




