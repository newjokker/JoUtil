# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import requests
import json


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}

r = requests.get('https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E5%9B%BE%E7%89%87&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=30&gsm=1e&1561022599290=',headers = headers).text

print(json.loads(r))

res = json.loads(r)['data']

for index,i in enumerate(res):
    url = i['hoverURL']
    print(url)
    with open( '{}.jpg'.format(index),'wb+') as f:
        f.write(requests.get(url).content)


