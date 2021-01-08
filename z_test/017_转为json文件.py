# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.deteRes import DeteRes
from JoTools.txkjRes.classifyRes import ClassifyResBase
from JoTools.utils.JsonUtil import JsonUtil
import json

img_path = r"C:\Users\14271\Desktop\del\img_xml\test.jpg"
xml_path = r"C:\Users\14271\Desktop\del\img_xml\test.xml"
json_path = r"C:\Users\14271\Desktop\del\img_xml\test.json"

# a = ClassifyResBase(assign_img_path=img_path, xml_path=xml_path)
a = DeteRes(assign_img_path=img_path, xml_path=xml_path)

json_dict = a.save_to_json()

# print(json_dict)


# test_dict = {"filename":"7ad5bb26-515d-11eb-b5ca-434c65a7bdff.jpg","folder":"/home/ldq/fzc_v0.2.3-A_new_flow/tmpfiles","object":"[\"{\\\"name\\\": \\\"fzc_yt\\\", \\\"prob\\\": 0.9983474016189575, \\\"id\\\": 0, \\\"bndbox\\\": {\\\"xmin\\\": 507, \\\"xmax\\\": 616, \\\"ymin\\\": 436, \\\"ymax\\\": 481}}\", \"{\\\"name\\\": \\\"fzc_other\\\", \\\"prob\\\": 0.7982571125030518, \\\"id\\\": 3, \\\"bndbox\\\": {\\\"xmin\\\": 947, \\\"xmax\\\": 1037, \\\"ymin\\\": 418, \\\"ymax\\\": 455}}\", \"{\\\"name\\\": \\\"fzc_other\\\", \\\"prob\\\": 0.6719563007354736, \\\"id\\\": 6, \\\"bndbox\\\": {\\\"xmin\\\": 159, \\\"xmax\\\": 275, \\\"ymin\\\": 494, \\\"ymax\\\": 557}}\"]","path":"/home/ldq/fzc_v0.2.3-A_new_flow/tmpfiles/7ad5bb26-515d-11eb-b5ca-434c65a7bdff.jpg","segmented":"","size":{"depth":"3","height":960,"width":1280},"source":""}
#
# # b = json.loads(test_dict)
# test_dict['path'] = None
#

aa = {'size': '{"height": 960, "width": 1280, "depth": "3"}', 'filename': '2c7bb87a-5169-11eb-b5ca-434c65a7bdff.jpg', 'path': None, 'object': '[]', 'folder': '/home/ldq/fzc_v0.2.3-A_new_flow/tmpfiles', 'segmented': '', 'source': ''}

b = DeteRes(json_dict=aa)
# print(test_dict)
print(b.save_to_json())
#
#
try:
    pass
except Exception as e:
    print(e)