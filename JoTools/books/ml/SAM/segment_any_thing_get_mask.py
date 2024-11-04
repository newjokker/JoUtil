# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import torch
import torchvision
import numpy as np
import torch
import matplotlib.pyplot as plt
import cv2
from segment_anything.utils.transforms import ResizeLongestSide
from segment_anything import sam_model_registry, SamPredictor
import random
import time
from torch.nn.functional import threshold, normalize
from JoTools.txkjRes.deteRes import DeteRes

img_path = r'/home/ldq/ucd_dir/nms/test4.jpg'
xml_path = r"/home/ldq/ucd_dir/nms/test4.xml"
sam_checkpoint = "/home/ldq/ucd_dir/nms/sam_vit_b_01ec64.pth"
# sam_checkpoint = "ok_49.pt"
model_type = "vit_b"
device = "cuda"

image = cv2.imread(img_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)

predictor = SamPredictor(sam)
predictor.set_image(image)


box = DeteRes(xml_path=xml_path)

if len(box) == 0:
    exit()

mask = np.zeros(image.shape[:2], dtype=np.bool)
for obj in box:
    each_mask, _, _ = predictor.predict(
        point_coords=None,
        box = np.array([obj.x1, obj.y1, obj.x2, obj.y2]),
        multimask_output=False,
    )
    each_mask = np.squeeze(each_mask)
    print(each_mask.shape)
    mask[obj.y1:obj.y2, obj.x1:obj.x2] = each_mask[obj.y1:obj.y2, obj.x1:obj.x2]
# exit()
a = mask.astype(int)
a = a * 255
a = a.astype(np.uint8)

# 找到轮廓
contours, _ = cv2.findContours(a, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 画出轮廓
cv2.drawContours(image, contours, -1, (0, 0, 255), 1)

cv2.imwrite("./res7149.jpg", image)











