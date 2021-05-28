import re
import requests
import json
import copy

"""
获取货币实时价格的代码
"""


def format_dollar_data(dollar_data):
    """对数据进行格式化"""
    # ['阿联酋迪拉姆', '', '169.13', '', '181.69', '175.07', '08:55:49']
    new_data = copy.deepcopy(dollar_data)
    for i in range(1, 6):
        new_data[i] = float(new_data[i]) if new_data[i] else -1
    return new_data

def get_real_time_data_from_web():
    """从网上实时获取数据"""
    url = 'http://www.boc.cn/sourcedb/whpj/'
    html = requests.get(url).content.decode("utf-8")    #  获取网页源码
    data = re.findall('<td>(.*?)</td>', html)           #  获取所有币种牌价
    # dollarData = data[-14:-7]                         #  获取美元牌价
    keys2 = ["货币名称", "现汇买入价", "现钞买入价", "现汇卖出价", "现钞卖出价", "中行折算价", "发布时间"]
    i, j = 0, 7

    item = []
    while True:
        dollarData = data[i:j]
        dollarData = format_dollar_data(dollarData)
        dictDollar = dict(zip(keys2, dollarData))
        item.append(dictDollar)
        i += 7
        j += 7
        if i == 189:
            break

    data = str(item).replace("'",'"')
    return data

def post_data(assign_data):
    """post 数据"""
    Post_url = "http://47.92.114.134:8000/zits/ztest"
    res = requests.post(url=Post_url, data=assign_data.encode('utf-8'))


if __name__ == "__main__":

    # get data
    dollar_data = get_real_time_data_from_web()
    # post data
    post_data(dollar_data)

