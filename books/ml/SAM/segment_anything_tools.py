# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import torch
import torchvision
import numpy as np
import matplotlib.pyplot as plt
import cv2
from segment_anything.utils.transforms import ResizeLongestSide
from segment_anything import sam_model_registry, SamPredictor
import random
from JoTools.txkjRes.deteRes import DeteRes
import time

# TODO 提取掩膜的范围，生成一个多边形

# FIXME 全图检测就是使用规则的网格点在全图上进行预测而已



def prepare_image(image, transform, device):
    image = transform.apply_image(image)
    image = torch.as_tensor(image, device=device.device)
    return image.permute(2, 0, 1).contiguous()



if __name__ == "__main__":

    # ------------------------------------------------------------------------------------------------------------------
    sam_checkpoint  = "/home/ldq/ucd_dir/nms/sam_vit_h_4b8939 (1).pth"
    model_type      = "vit_h"
    # sam_checkpoint  = "/home/ldq/ucd_dir/nms/sam_vit_b_01ec64.pth"
    # model_type      = "vit_b"
    device          = "cuda"
    img_path        = r'/home/ldq/ucd_dir/nms/img_xml/Dcp0759.jpg'
    xml_path        = r"/home/ldq/ucd_dir/nms/img_xml/Dcp0759.xml"
    # ------------------------------------------------------------------------------------------------------------------

    image = cv2.imread(img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    h, w = image.shape[:2]

    sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
    sam.to(device=device)
    predictor = SamPredictor(sam)
    predictor.set_image(image)


    # get boxes
    boxes = []
    dete_res = DeteRes(xml_path)
    for obj in dete_res:
        boxes.append([obj.x1, obj.y1, obj.x2, obj.y2])

    # get points
    points = []
    point_labels = []
    numb = 0
    M, N = 10, 10
    for i in range(M):
        for j in range(N):
            points.append([int(i*(w/M)), int(j*(h/N))])
            numb += 1
            point_labels.append(numb)
    #

    image_boxes     = torch.tensor(boxes, device=sam.device)
    points          = torch.tensor(points, device=sam.device)
    point_labels    = torch.tensor(point_labels, device=sam.device)
    resize_transform = ResizeLongestSide(sam.image_encoder.img_size)

    print(resize_transform.apply_coords_torch(points, image.shape[:2]).shape)
    print(resize_transform.apply_coords_torch(points, image.shape[:2]))
    print(resize_transform.apply_boxes_torch(image_boxes, image.shape[:2]).shape)
    print(resize_transform.apply_boxes_torch(image_boxes, image.shape[:2]))

    batched_input = [
        {
            # 'point_coords' : resize_transform.apply_coords_torch(points, image.shape[:2]),
            # 'point_labels' : resize_transform.apply_coords_torch(point_labels, image.shape[:2]),
            'image': prepare_image(image, resize_transform, sam),
            # 'boxes': resize_transform.apply_boxes_torch(image_boxes, image.shape[:2]),
            'original_size': image.shape[:2]
        }
    ]
    # inferernce
    start = time.time()
    batched_output = sam(batched_input, multimask_output=False)
    stop = time.time()
    print("* use time : {0} s".format(stop - start))

    # color mask
    for mask in batched_output[0]['masks']:
        image[mask.cpu().numpy()[0, :, :], :] = [random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)]

    # save res
    cv2.imwrite("./res3.jpg", image)
















