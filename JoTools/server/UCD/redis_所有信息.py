# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import redis

def print_redis_info(redis_client):
    # 查看数据库的大小（键的数量）
    db_size = redis_client.dbsize()
    print(f"数据库大小（键的数量）：{db_size}")

    # 查看所有键
    all_keys = redis_client.keys("*")
    print("所有键：")
    for key in all_keys:
        print(f"  {key}")

    # 查看所有键的类型和值
    print("所有键的类型和值：")
    for key in all_keys:
        key_name = key
        key_type = redis_client.type(key_name)
        key_value = redis_client.get(key_name) if key_type == "string" else None
        print(f"  键：{key_name}，类型：{key_type}，值：{key_value}")

    # # 查看 Redis 服务器信息
    # server_info = redis_client.info()
    # print("Redis 服务器信息：")
    # for key, value in server_info.items():
    #     if isinstance(value, dict):
    #         print(f"  {key}:")
    #         for sub_key, sub_value in value.items():
    #             print(f"    {sub_key}: {sub_value}")
    #     else:
    #         print(f"  {key}: {value}")

if __name__ == "__main__":

    # 连接到 Redis
    # r = redis.Redis(host='192.168.3.221', port=6379, db=0)
    redis_client = redis.StrictRedis(host='192.168.3.221', port=6379, decode_responses=True)

    # 打印 Redis 信息
    print_redis_info(redis_client)
