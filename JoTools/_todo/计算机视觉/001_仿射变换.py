# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from scipy import ndimage
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img_path = r"C:\Users\14271\Desktop\del\test.png"
im = np.array(Image.open(img_path).convert('L'))
# 有着 6 个自由度的仿射变换
H = np.array([[2, 0.1, -300], [0.1, 2, -300], [0, 0, 1]])
im2 = ndimage.affine_transform(im, H[:2, :2], (H[0, 2], H[1, 2]))

plt.figure()
plt.gray()
plt.imshow(im2)
plt.show()

