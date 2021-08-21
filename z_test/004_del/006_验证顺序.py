

import ee

ee.Authenticate()

##ee.Initialize()


import datetime
import requests
import uuid


#each_img_path = r"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fattach.bbs.miui.com%2Fforum%2F201209%2F18%2F1750038ve0hhe9vk8dhv8z.jpg&refer=http%3A%2F%2Fattach.bbs.miui.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1630756166&t=8b336617b971e5cbc6975c454fb98905"
# each_img_path = r"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fattach.bbs.miui.com%2Fforum%2F201209%2F18%2F1750038ve0hhe9vk8dhv8z.jpg&refer=http%3A%2F%2Fattach.bbs.miui.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1630756166&t=8b336617b971e5cbc6975c454fb98905"
# each_img_path = r"http://wx4.sinaimg.cn/mw600/622fd6d1gy1gtcp9fk58nj20d80j9435.jpg"
each_img_path = r"http://192.168.3.109:7002/images/2021-08-12/1425661616862588929/8634ac53c3c94ed5b3189560cc6698be.jpg"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
}

save_path = ".{0}.jpg".format(str(uuid.uuid1()))
f = requests.get(each_img_path, headers=headers)

with open(save_path, "wb") as file_url:
    file_url.write(f.content)



