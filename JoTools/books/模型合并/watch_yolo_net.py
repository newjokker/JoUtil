# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import torch
import collections
from saturn_lib.yolov56Detection import YOLOV56Detection


save_path   = "combine_yolo_base.pth"
cuda_info   = "cuda:0"
device      = torch.device(cuda_info)

# ----------------------------------------------------------------------------------------------------------------------

model_path = r"/home/ldq/yolov5/runs/test.pt"
model_path = r"/home/ldq/txkj_lib/yolo_data/alltgtSD_yolo5_65L_V8.pt"

base = torch.load(model_path, map_location=device)
keys = base["model"].state_dict().keys()

print(keys)

