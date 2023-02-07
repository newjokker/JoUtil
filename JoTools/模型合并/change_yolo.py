# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import torch
import collections
# from saturn_lib.yolov5Detection import YOLOV5Detection



model_path_list = [
    #r"/home/ldq/txkj_lib/yolo_data/alltgtSD_yolo5_65L_V8_21epoch.pt",
    #r"/home/ldq/txkj_lib/yolo_data/alltgtSD_yolo5_65L_V8_50epoch.pt",
    r"C:/Users/14271/Desktop/test.pt",
    r"/home/ldq/txkj_lib/yolo_data/alltgtSD_yolo5_65L_V8_92epoch.pt",
]

save_path   = "combine_yolo_base.pth"
cuda_info   = "cpu"
device      = torch.device(cuda_info)

# ----------------------------------------------------------------------------------------------------------------------

# if len(model_path_list) < 2:
#     raise ValueError("模型路径太少，模型合并至少需要两个模型")
#
# model_num = len(model_path_list)
# base = torch.load(model_path_list[0], map_location=device)
# # keys = base.state_dict().keys()
# keys = base["model"].state_dict().keys()
#
# res = collections.OrderedDict()


base = torch.load(model_path_list[0], map_location=device)

# print(type(a["model"]))
#
# for each in a["model"].state_dict():
#     print(each)
#
# base = torch.load("./checkpoints/yolov5s.pt", map_location=torch.device("cuda:0"))

new_dict = dict(base["model"].state_dict())
for key,value in  base["model"].state_dict().items():
    if key == 'model.0.conv.conv.weight':
        key = 'model.0.convx.conv.weight'
    elif key == 'model.0.conv.bn.weight':
        key = 'model.0.convx.bn.weight'
    elif key == 'model.0.conv.bn.bias':
        key = 'model.0.convx.bn.bias'
    elif key == 'model.0.conv.bn.running_mean':
        key = 'model.0.convx.bn.running_mean'
    elif key == 'model.0.conv.bn.running_var':
        key = 'model.0.convx.bn.running_var'
    elif key == 'model.0.conv.bn.num_batches_tracked':
        key = 'model.0.convx.bn.num_batches_tracked'
    new_dict[key] = value

# base["model"].state_dict().update(new_dict)


torch.save(new_dict, "change_yolo.pth")


# print(new_dict.keys())
print(base["model"].state_dict().keys())

#
# for each in base["model"].state_dict():
#     print(each)

# print(type(a))

#
# model_list = []
#
# # load all models
# for each_model_path in model_path_list:
#     model_list.append(torch.load(each_model_path, map_location=device))
#
# # combine all models
# for each_k in keys:
#     each_res = model_list[0]["model"].state_dict()[each_k]
#     # print("-" * 100)
#
#     if isinstance(each_res, torch.Tensor):
#         print(each_k, "----------------------->", each_res.shape)
#     else:
#         print(each_k)
#
#     for each_model in model_list[1:]:
#         if isinstance(each_res, torch.Tensor) and "tracked" not in each_k:
#             if "model.24" in each_k:
#                 each_res += each_model["model"].state_dict()[each_k]
#                 each_res /= model_num
#                 res[each_k] = each_res
#
# for each_k in keys:
#     if each_k in res:
#         model_list[0]["model"].state_dict()[each_k] = res[each_k]
# model_list
# torch.save([0], save_path)

