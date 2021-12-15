# -*- coding: utf-8  -*-
# -*- author: jokker -*-



from JoTools.txkjRes.pointRes import PointRes
from JoTools.txkjRes.deteObj import PointObj

img_path = r"C:\Users\14271\Desktop\关键点\images.jpg"
json_path = r"C:\Users\14271\Desktop\关键点\images.json"
json_path_save = r"C:\Users\14271\Desktop\关键点\images_new.json"


# a = PointRes(json_path=json_path)
#
#
# a.img_path = img_path
#
#
# a.print_as_fzc_format()
#
# a.filter_by_tags(['p1', 'p2'])
#
# a.save_to_json_file(json_path_save, include_img_data=True)
#
# a.print_as_fzc_format()
#
# a.draw_res(r"C:\Users\14271\Desktop\关键点\images_draw.jpg")


a = PointRes()
a.img_path = img_path


a.print_as_fzc_format()
print('-'*50)
a.filter_by_tags(['p1', 'p2'])


# a.version = "4.4.0"
# a.image_width = '100'
# a.image_height = '100'
# a.img_name = '100'

a.add_obj(12,12,'new', 0.5)

each_point_obj = PointObj(12,34,'new', 0.3)
a.add_obj_2(each_point_obj)

a.print_as_fzc_format()


a.save_to_json_file(r"C:\Users\14271\Desktop\关键点\images_00.json", include_img_data=True)

a.draw_res(r"C:\Users\14271\Desktop\关键点\images_new.jpg")
