# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import redis



def add_info_to_assign_key(key, value):
    r = redis.Redis(host='192.168.3.221', port=6379, db=0)
    a = r.hget("official", key)
    if a is not None:
        a = a.decode('utf-8')
        info_set = set(a.split("-+-"))
        info_set.add(value)
        info_list = list(info_set)
        a = "-+-".join(info_list)
    else:
        a = value
    _insert_to_official(key, a)

def _insert_to_official(key, value):
    r = redis.Redis(host='192.168.3.221', port=6379, db=0)
    b = r.hset("official", key, value)
    return b

def get_info_from_official(key):
    r = redis.Redis(host='192.168.3.221', port=6379, db=0)
    a = r.hget("official", key)
    print(a.decode("utf-8"))

def get_all_info_from_official():
    r = redis.Redis(host='192.168.3.221', port=6379, db=0)
    a = r.hgetall("official")
    for each in a:
        print(each.decode('utf-8'), ":")
        for i in a[each].decode('utf-8').split("-+-"):
            print("    * ", i)

def remove_info_from_official(key):
    r = redis.Redis(host='192.168.3.221', port=6379, db=0)
    r.hdel("official", key)



if __name__ == "__main__":

# 公司名称：南京土星信息科技有限公司
# 纳税人识别号：91320114MA1MYQX21D
# 地址：南京市建邺区贤坤路1号科创中心3楼325室
# 公司电话：025-57039152
# 开户行：南京银行股份有限公司清凉门支行    
# 账户：0173230000000021

    # add_info_to_assign_key("111密码", "miaoyu (chart gpt4) : X61c4m4")


    # add_info_to_assign_key("wifi 密码", "土星科技 : None")
    add_info_to_assign_key("电力信息外包", "11楼生产环境电脑密码 : !QA2ws3ed")

    # remove_info_from_official("公司信息")

    get_all_info_from_official()





