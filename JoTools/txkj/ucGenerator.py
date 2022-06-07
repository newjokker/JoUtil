# -*- coding: utf-8  -*-
# -*- author: jokker -*-


""" UC 生成器，输入 md5 返回对应的 UC"""

import uuid


# todo 创建自己的 UC 规则
# todo 将 UC 的位数设置为每天 1000 * 1000 * 1000 位数
# todo 其实限制每一秒只分配一个 UC 即可，知道分配 UC 的时间点 + MD5 就能唯一地确定这个 UC
# todo UC 中包含文件的类型信息 + 时间信息
# todo 析构函数能在出意外的时候保存 新申请的 UC dict

# todo 是否可以使用 resids 代替数据库


# fixme json 的定位是记录所有的数据，没有其他所有部分，依靠 json 和 data 能全部恢复
# fixme redis 等数据库的定位在于更快地执行（1）更快地获取 UC （2）更快地查询标签 UC 等




class UCGenerator(object):
    """与redis深度绑定"""

    def __init__(self, host, port):
        # fixme 用于存储历史 UC，
        self._host = host
        self._port = port

    def get_uc(self, md5):
        uc = None
        return uc


class RedisInfo(object):
    """用于快速查询json中的信息"""

    # fixme 使用 redis 的五张表就能代替 mysql
    # fixme MD5 hash 用于查询 md5 是否有被使用过
    # fixme UC-MD5 哈希表
    # fixme tags set 表
    # fixme tag-uc set 表，
    # fixme -tag-uc set 表，标记某一个标签不存在某一个 UC 中
    # fixme 一个记录数据类型的表，jpg JPG PNG 等等，用于快速获取数据类型
    # todo 是否还需要，某张表中不存在某一标签这个功能？这个信息在 json 中存放着


# todo 一百万条数据 只有 40M，

a = {}

for i in range(1000 * 1000):
    a[str(uuid.uuid1())] = "test_UC_path"


print(a.__sizeof__())
print(a.__sizeof__()/1024/1024)








