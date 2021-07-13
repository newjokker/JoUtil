# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import pickle
import redis
import cv2
import numpy as np
import time
import random


class RedisUtil:

    def __init__(self):
        self.conn = redis.Redis(host='192.168.3.185', port=6379)

    def insert_image(self, frame_id, img_path):
        # 将图片序列化存入redis中
        start_time = time.time()
        frame = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)
        after_read = time.time()
        b = pickle.dumps(frame)  # frame is numpy.ndarray
        self.conn.set(frame_id, b)
        after_insert = time.time()
        return after_read - start_time, after_insert - after_read

    def get_image(self, frame_id):
        # 从redis中取出序列化的图片并进行反序列化
        start_time = time.time()
        a = pickle.loads(self.conn.get(frame_id))
        print(a.shape)
        return time.time() - start_time


if __name__ == "__main__":

    read_time_list, insert_time_list, get_time_list = [], [], []
    img_path = r"/home/ldq/del/test.jpg"
    a = RedisUtil()

    for i in range(100):
        random_id = str(random.random())
        each_read_time, each_insert_time = a.insert_image(random_id, img_path)
        read_time_list.append(each_read_time)
        insert_time_list.append(each_insert_time)
        get_time = a.get_image(random_id)
        get_time_list.append(get_time)

    print(sum(read_time_list))
    print(sum(insert_time_list))
    print(sum(get_time_list))



