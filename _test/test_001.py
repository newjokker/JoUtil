# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.for_csdn.word_pic.word_pic import WordImage
from PIL import Image


# -------------------------------------------------------------------------------------
ratio = 2                                               # 图像缩小的比例
img_path = r"C:\Users\14271\Desktop\test.jpg"
save_path = r'C:\Users\14271\Desktop\test_2.jpg'
# -------------------------------------------------------------------------------------

img = Image.open(img_path)
width, height = img.size
new_width, new_height = int(width/ratio), int(height/ratio)

a = WordImage(img_path, new_size = (new_width, new_height))
a.analysis_pkl_path = r'C:\Algo\jo_util\JoTools\for_csdn\word_pic\data\del.pkl'
a.save_path = save_path
a.do_process()

# todo 分为三个部分，（1）汉字转为对应的图库中的图片（2）对拥有的图库进行分析，参数可视化（3）指定图片得到对应的汉字图
# todo 使用全部汉字得到的图片结果反而不好，找到原因，并分析时候需要进行修改
# todo 对各个灰度做统计，得到对应的数字的个数



