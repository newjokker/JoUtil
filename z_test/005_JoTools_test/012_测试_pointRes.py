# -*- coding: utf-8  -*-
# -*- author: jokker -*-



from JoTools.txkjRes.pointRes import PointRes


img_path = r"C:\Users\14271\Desktop\关键点\images.jpg"
json_path = r"C:\Users\14271\Desktop\关键点\images.json"
json_path_save = r"C:\Users\14271\Desktop\关键点\images_new.json"


a = PointRes(json_path=json_path)


a.img_path = img_path

a.save_to_json_file(json_path_save, include_img_data=True)
