# -*- coding: utf-8  -*-
# -*- author: jokker -*-

# refer : https://www.liaoxuefeng.com/wiki/1016959663602400/1017592449371072


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

    def check(self, balue):
        pass

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

    def check(self, value):
        if isinstance(value, str):
            return True
        else:
            return False

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

    def check(self, value):
        if isinstance(value, int):
            return True
        else:
            return False

class ModelMetaclass(type):
    # 名字，父类，属性值
    def __new__(mcs, name, bases, attrs):
        if name=='Model':
            return type.__new__(mcs, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings                        # 保存属性和列的映射关系，fixme 这个是用于存储类属性的字典吗？
        attrs['__table__'] = name                               # 假设表名和类名一致
        return type.__new__(mcs, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        for each_key in kw:
            if each_key not in self.__mappings__:
                raise ValueError("{0} was not define".format(each_key))
            if not self.__mappings__[each_key].check(kw[each_key]):
                raise ValueError("{0} 's type should be {1} not {2}".format(each_key, self.__mappings__[each_key], type(kw[each_key])))

        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
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


class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
    is_ok = StringField('is_ok')
    #
    new=StringField('new')


if __name__ == "__main__":

    # 动态创建类，（1）指定类中属性的个数，是否可添加属性等（2）指定类中属性的类型

    u1 = User(id=12345, name='Michael', email='test@orm.org', password='123456')
    u2 = User(id = 112, name='jokker', email='hehe', new = '4564')











