# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import torch

cuda_info   = "cpu"
device      = torch.device(cuda_info)

base = torch.load(r"C:\Users\14271\Desktop\yolov5\yolov5x.pt", map_location=device)

