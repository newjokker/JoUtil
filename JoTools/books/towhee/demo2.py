# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from towhee import pipe, ops

img_embedding = (
    pipe.input('url')
        .map('url', 'img', ops.image_decode.cv2())
        .map('img', 'embedding', ops.image_embedding.timm(model_name='resnet50'))
        .output('embedding')
)

url = 'https://github.com/towhee-io/towhee/raw/main/towhee_logo.png'
res = img_embedding(url).get()