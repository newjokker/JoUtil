# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.for_csdn.word_pic.word_pic import WordImage
from PIL import Image

ratio = 2  # 图像缩小的比例
img_path = r"C:\Users\14271\Desktop\del\red.png"
save_path = r"C:\Users\14271\Desktop\del\test_new.jpg"
# -------------------------------------------------------------------------------------

img = Image.open(img_path)
width, height = img.size
new_width, new_height = int(width / ratio), int(height / ratio)

a = WordImage(img_path, new_size=(new_width, new_height))
a.analysis_pkl_path = r'C:\Algo\jo_util\JoTools\for_csdn\word_pic\data\del.pkl'
a.save_path = save_path
a.do_process()

