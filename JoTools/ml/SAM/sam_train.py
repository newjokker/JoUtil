import os
import glob
import torch
import numpy as np
import cv2
from segment_anything.utils.transforms import ResizeLongestSide
from segment_anything import sam_model_registry, SamPredictor
from statistics import mean

num_epochs = 10

# 定义模型路径和需要训练的图片所在文件夹路径
model_path = r"./sam_vit_b_01ec64.pth"
img_folder_path = r"./cs_del/images"
npy_folder_path = r"./cs_del/masks"
device = "cpu"

# 定义模型
sam_model = sam_model_registry['vit_b'](checkpoint=model_path)
sam_model.to(device=device)
sam_model.train()


# FIXME 在训练的时候是需要指定目标的范围的，不指定训练效果不好

# 定义训练超参数
lr = 1e-4
wd = 0
optimizer = torch.optim.Adam(sam_model.mask_decoder.parameters(), lr=lr, weight_decay=wd)
loss_fn = torch.nn.MSELoss()

# 加载所有图片和对应的掩膜
image_paths = sorted(glob.glob(os.path.join(img_folder_path, '*.jpg')))
mask_paths = sorted(glob.glob(os.path.join(npy_folder_path, '*.npy')))
assert len(image_paths) == len(mask_paths), "Number of images and masks should be same"

for epoch in range(num_epochs):  # 训练 100 个 epoch

    epoch_losses = []

    for img_path, mask_path in zip(image_paths, mask_paths):
        print(img_path, mask_path)
        # 读取图片并进行预处理
        image = cv2.imread(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        transform = ResizeLongestSide(sam_model.image_encoder.img_size)
        input_image = transform.apply_image(image)
        input_image_torch = torch.as_tensor(input_image, device=device)
        transformed_image = input_image_torch.permute(2, 0, 1).contiguous()[None, :, :, :]
        input_image = sam_model.preprocess(transformed_image)
        original_size = image.shape[:2]
        input_size = tuple(transformed_image.shape[-2:])

        # 读取掩膜并将其转换为二进制掩膜
        gt_binary_mask = torch.unsqueeze(torch.unsqueeze(torch.as_tensor(np.load(mask_path), dtype=torch.float32), dim=0), dim=0)

        # 计算预测的二进制掩膜
        with torch.no_grad():
            image_embedding = sam_model.image_encoder(input_image)
            sparse_embeddings, dense_embeddings = sam_model.prompt_encoder(
                points=None,
                boxes=None,
                masks=None,
            )

        low_res_masks, iou_predictions = sam_model.mask_decoder(
            image_embeddings=image_embedding,
            image_pe=sam_model.prompt_encoder.get_dense_pe(),
            sparse_prompt_embeddings=sparse_embeddings,
            dense_prompt_embeddings=dense_embeddings,
            multimask_output=False,
        )

        upscaled_masks = sam_model.postprocess_masks(low_res_masks, input_size, original_size).to(device)

        # 计算损失并进行反向传播
        loss = loss_fn(upscaled_masks, gt_binary_mask)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        epoch_losses.append(loss.item())

    print(f'EPOCH: {epoch}')
    print(f'Mean loss: {mean(epoch_losses)}')

torch.save(sam_model.state_dict(), r"ok.pt")
