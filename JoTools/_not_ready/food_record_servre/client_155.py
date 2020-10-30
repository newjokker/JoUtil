# -*- coding: utf-8  -*-
# -*- author: jokker -*-


# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import requests

"""
* 测试模型训练是否可用
"""


# ---------------------------------------------------- 训练 ------------------------------------------------------------

# url = 'http://192.168.3.110:8084/training/'
url = r'http://192.168.3.155:5444/demo'


while True:

    eat_info = input("eat info :")

    d = {
        "eat_info":eat_info,
    }

    r = requests.post(url, data=d)

    print(r.text)
    print(r)

# ----------------------------------------------------------------------------------------------------------------------

# fixme 检测图片只需要完善 request.form['datatype'] 和  request.files['image'].filename 两个即可，
