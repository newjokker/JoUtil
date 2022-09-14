# -*- coding: utf-8  -*-
# -*- author: jokker -*-




# from requests_toolbelt import MultipartEncoder
# import requests
# import httplib2
#
#
# data = MultipartEncoder(fields={'file': ('filename', open(r'C:\Users\14271\Desktop\del\save_img\img\Dsn06b3.jpg', 'rb'), 'text/xml')})
#
#
# response = requests.post("http://192.168.3.221:1234/test", files={"file": "bar"}, data={"file": "hele"})
#
# print(response.text)
#
# # requests.post(url="http://192.168.3.221:1234/test", data={"file": "123"}, headers={ 'Content-Type': data.content_type})



from JoTools.utils.MySqlUtil import MySqlUtil

a = MySqlUtil()

res = a.conoect_mysql("192.168.3.221", 3306, "root", "txkj", "dete_res", charset='utf8')


print(res)












