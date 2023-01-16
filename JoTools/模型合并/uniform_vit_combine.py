# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import torch
import collections

# ----------------------------------------------------------------------------------------------------------------------

# model_path_list = [
#     r"/home/ldq/txkj_lib/vit_data/kkxLM_3cls_0_3_0.pth",
#     r"/home/ldq/txkj_lib/vit_data/kkxLM_3cls_0_3_2.pth",
#     r"/home/ldq/txkj_lib/vit_data/kkxLM_3cls_0_3_3.pth",
#     r"/home/ldq/txkj_lib/vit_data/kkxLM_3cls_0_3_5.pth",
#     r"/home/ldq/txkj_lib/vit_data/kkxLM_3cls_0_3_6.pth",
# ]

model_path_list = [
    r"/home/ldq/txkj_lib/vit_data/rust_vit_0_1_4.pth",
    r"/home/ldq/txkj_lib/vit_data/rust_vit_0_1_5.pth",
    r"/home/ldq/txkj_lib/vit_data/rust_vit_0_1_6.pth",
    r"/home/ldq/rust_test/models/seed_04.pth",
]

save_path   =     r"/home/ldq/rust_test/models/combine_seed_016.pth",

cuda_info   = "cuda:0"
device      = torch.device(cuda_info)

# ----------------------------------------------------------------------------------------------------------------------

if len(model_path_list) < 2:
    raise ValueError("模型路径太少，模型合并至少需要两个模型")

model_num = len(model_path_list)
base = torch.load(model_path_list[0], map_location=device)
keys = base.keys()
res = collections.OrderedDict()
model_list = []

# load all models
for each_model_path in model_path_list:
    model_list.append(torch.load(each_model_path, map_location=device))

# combine all models
for each_k in keys:
    each_res = model_list[0][each_k]
    for each_model in model_list[1:]:
        if each_k in each_model:
            each_res += each_model[each_k]
        else:
            each_res += each_model["module." + each_k]

    each_res /= model_num
    res[each_k] = each_res

torch.save(res, save_path)


