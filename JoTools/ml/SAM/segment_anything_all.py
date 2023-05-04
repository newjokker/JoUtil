# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import numpy as np
import torch
import matplotlib.pyplot as plt
import cv2
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor
import random
from JoTools.utils.FileOperationUtil import FileOperationUtil

# ----------------------------------------------------------------------------------------------------------------------

img_dir     = r"/home/ldq/ucd_dir/nms/cs_del/images"
save_dir    = r"/home/ldq/ucd_dir/nms/draw"
model_path  = r"/home/ldq/ucd_dir/nms/ok.pt"
model_type  = "vit_b"    # vit_b, vit_h
device = "cuda"

# ----------------------------------------------------------------------------------------------------------------------


# load model
sam_checkpoint = model_path
sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)

# inference
mask_generator = SamAutomaticMaskGenerator(
    model=sam,
    points_per_side=32,
    pred_iou_thresh=0.86,
    stability_score_thresh=0.92,
    crop_n_layers=1,
    crop_n_points_downscale_factor=2,
    min_mask_region_area=100
)

for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=[".jpg"]):

    save_path = os.path.join(save_dir, os.path.split(each_img_path)[1])

    if os.path.exists(save_path):
        print("* 文件重复")
        continue

    if os.path.getsize(each_img_path) / 1024 > 500:
        print("* 文件太大")
        continue

    if os.path.getsize(each_img_path) / 1024 < 50:
        print("* 文件太小")
        continue

    print(each_img_path)

    # read img
    image = cv2.imread(each_img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    masks = mask_generator.generate(image)

    # draw
    sorted_anns = sorted(masks, key=(lambda x: x['area']), reverse=True)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2RGBA)
    overlay = np.zeros((image.shape[0], image.shape[1], 4), dtype=np.uint8)

    for ann in sorted_anns:
        m = ann['segmentation']
        overlay[m,:] = [random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), 100]
    image = cv2.addWeighted(image, 1, overlay, 0.5, 0)
    cv2.imwrite(save_path, image)






