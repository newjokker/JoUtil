# -*- coding: utf-8  -*-
# -*- author: jokker -*-


""" UC 生成器，输入 md5 返回对应的 UC"""

import uuid
import redis
import datetime
from JoTools.utils.DecoratorUtil import DecoratorUtil

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

    # todo UC 标志日期的前三位表示，自土星成立之日起到现在的天数，转为 24 + 10 进制（或许不美观，还是直接用一搏那个方式比较好）
    # todo 后面直接是 34 ** 5 张图片, 45,435,424 左右

    def __init__(self, host, port):
        # fixme 用于存储历史 UC，
        self._host = host
        self._port = port

    def get_uc(self, md5):
        uc = None
        return uc


class RedisInfo(object):
    """用于快速查询 json 中的信息"""

    # fixme 使用 redis 的五张表就能代替 mysql
    # fixme MD5 hash 用于查询 md5 是否有被使用过
    # fixme UC-MD5 哈希表
    # fixme tags set 表
    # fixme tag-uc set 表，
    # fixme -tag-uc set 表，标记某一个标签不存在某一个 UC 中
    # fixme 一个记录数据类型的表，jpg JPG PNG 等等，用于快速获取数据类型
    # todo 是否还需要，某张表中不存在某一标签这个功能？这个信息在 json 中存放着

    def __init__(self, host, port):
        self._host = host
        self._port = port
        self.r = redis.StrictRedis(host=host, port=port, decode_responses=True)
        #
        self._init_redis()

    @DecoratorUtil.time_this
    def _init_redis(self):
        """初始化 redis 中的表"""

        # 貌似这些表根本不需要初始化，没有数据会直接返回 None

        # MD5_UC
        if "MD5_UC" not in self.r.keys():
            self.r.hset('MD5_UC', 'md5', 'uc')
        # MD5_set
        if "MD5_SET" not in self.r.keys():
            self.r.sadd("MD5_SET", 'md5_demo')
        # UC_set
        if "UC_SET" not in self.r.keys():
            self.r.sadd("UC_SET", 'uc_demo')
        # tags
        if "TAG_SET" not in self.r.keys():
            self.r.sadd("TAG_SET", "demo")
        # TAG_UC
        if "TAG_UC" not in self.r.keys():
            self.r.hset("TAG_UC", "tag_demo", "uc_demo")
        # UC_SUFFIX
        if "UC_SUFFIX" not in self.r.keys():
            self.r.hset("UC_SUFFIX", "uc_demo", "suffix_demo")

        print(self.r.keys())


    def _add_md5(self, md5):
        """插入 md5"""

        # todo 根据 hash 和 时间 得到一个 UC，
        # todo UC 已存在继续碰撞
        region_md5 = md5
        now = datetime.datetime.now()
        year, month, day = now.year, now.month, now.day
        uc_part1 = "001"
        while True:
            uc_part2 = hash(md5) % 10000
            uc = uc_part1 + uc_part2
            if self.r.sismember('UC_SET', uc):
                md5 += str(uuid.uuid1())
            else:
                p_1 = self.r.hset('MD5_UC', region_md5, uc)
                p_2 = self.r.sadd('MD5_SET', region_md5)
                p_3 = self.r.sadd('UC_SET', uc)
                # fixme 如果三个操作有任意一个失败，直接回滚上面的操作

    def get_uc(self, md5):
        """增加一个 md5 获取一个 UC"""
        if md5 not in self.r.sismember('MD5_SET', md5):
            self._add_md5(md5)
        return self.r.hget('MD5_UC', md5)


if __name__ == "__main__":

    a = RedisInfo('192.168.3.221', '6379')






