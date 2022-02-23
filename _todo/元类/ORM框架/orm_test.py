# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# refer : https://www.liaoxuefeng.com/wiki/1016959663602400/1017592449371072


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')
        # print(name, str)

        # if not isinstance(name, str):
        #     raise ValueError("需要输入字符串类型")

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    # 名字，父类，属性值
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        # fixme 删除不需要的类属性，将类属性信息放到 attrs['__mappings__'] 中去，使用 User.name 会报错，因为类属性已经给删除了
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings                        # 保存属性和列的映射关系，fixme 这个是用于存储类属性的字典吗？
        attrs['__table__'] = name                               # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


# fixme model 继承的是个字典，所有有 如 self[key]的使用方法
class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        # fixme 这边是设置的类属性？不是，因为继承的是个字典
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append(str(getattr(self, k, None)))
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)



# fixme 这边需要动态地定义多种类型，所以能动态对类进行修改，确实相当方便
class User(Model):
    # fixme 这边的类属性到后面就会变成实例属性，
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
    is_ok = StringField('is_ok')


if __name__ == "__main__":

    # fixme 设置属性的行为是本身 model 继承的 dict 类就有的功能
    u1 = User(id="12345", name='Michael', email='test@orm.org', password=5)

    u1.is_ok = False

    u1.save()

    print(User.name)









