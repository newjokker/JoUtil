# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.deteRes import DeteRes


img_path = r"C:\Users\14271\Desktop\del\del\35KV大新线仙临支线25号右地线小号侧U型挂环缺销钉-DJI_0746.jpg"
xml_path = r"C:\Users\14271\Desktop\del\del\35KV大新线仙临支线25号右地线小号侧U型挂环缺销钉-DJI_0746.xml"
save_dir = r"C:\Users\14271\Desktop\del\crop"

# a = DeteRes()
# a.img_path = img_path
# a.xml_path = xml_path
#
# a.crop_and_save(save_dir)
# json_str = a.save_to_json()

json_str = {'path': None, 'folder': '', 'filename': '', 'object': '["{\\"id\\": -1, \\"prob\\": 0.9894399046897888, \\"bndbox\\": {\\"xmax\\": 1383, \\"ymax\\": 3376, \\"xmin\\": 1153, \\"ymin\\": 3290}, \\"name\\": \\"fzc_yt\\"}"]', 'size': '{"depth": "3", "width": -1, "height": -1}', 'source': '', 'segmented': ''}
b = DeteRes(json_dict=json_str)

print(b)


for each in b.get_fzc_format():
    print(each)
























