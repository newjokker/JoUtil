# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from deep_sort.utils.parser import get_config
from deep_sort.deep_sort import DeepSort
from deep_sort.deep_sort.deep.feature_extractor import Extractor
from deep_sort.deep_sort.sort.nn_matching import NearestNeighborDistanceMetric
from deep_sort.deep_sort.sort.preprocessing import non_max_suppression
from deep_sort.deep_sort.sort.detection import Detection
from deep_sort.deep_sort.sort.tracker import Tracker
import argparse
import os
import platform
import shutil
import time
from pathlib import Path
import cv2
import torch
import torch.backends.cudnn as cudnn
# https://github.com/pytorch/pytorch/issues/3678
import sys
from lib.detect_libs.yolo5Detection import YOLO5Detection
import queue as Queue
import subprocess as sp
from multiprocessing import Process, Manager
import gc
import threading
from timeit import time
import numpy as np

q = Queue.Queue()


def parse_args():
    parser = argparse.ArgumentParser(description='Tensorflow Faster R-CNN demo')
    parser.add_argument('--gpuID', dest='gpuID', type=int, default=0)
    parser.add_argument('--port', dest='port', type=int, default=5444)
    parser.add_argument('--gpuRatio', dest='gpuRatio', type=float, default=0.1)
    parser.add_argument('--host', dest='host', type=str, default='127.0.0.1')
    parser.add_argument('--logID', dest='logID', type=str, default='0')
    parser.add_argument('--objName', dest='objName', type=str, default='aqm')
    args = parser.parse_args()

    return args


# 重写MyThread.py线程类，使其能够返回值
class MyThread(threading.Thread):
    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args
        self.result = self.func(*self.args)

    def get_result(self):
        # 必须等待线程执行完毕,如果线程还未执行完毕就去获取result是没有结果的
        threading.Thread.join(self)
        try:
            return self.result
        except Exception:
            return None


'''
python多进程：
receive：该进程接收图片
realse：该进程处理图片，进行检测
'''


def receive(stack):
    top = 100
    # url = ' '
    video_capture = cv2.VideoCapture("水口-检修平台下游侧.ts")
    # ret, frame = video_capture.read()
    while True:
        ret, frame = video_capture.read()
        if ret:
            stack.append(frame)
            if len(stack) >= top:
                # print('Stack is full.........')
                del stack[:50]
                gc.collect()


def realse(stack):
    rtmpUrl = "rtsp://192.168.3.202/live"

    args = parse_args()
    objName = args.objName

    scriptName = os.path.basename(__file__).split('.')[0]

    model = YOLO5Detection(args, objName, scriptName)
    model.model_restore()

    cfg = get_config()
    cfg.merge_from_file("deep_sort/configs/deep_sort.yaml")
    deepsort = DeepSort(cfg.DEEPSORT.REID_CKPT,
                        max_dist=cfg.DEEPSORT.MAX_DIST, min_confidence=cfg.DEEPSORT.MIN_CONFIDENCE,
                        nms_max_overlap=cfg.DEEPSORT.NMS_MAX_OVERLAP, max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE,
                        max_age=cfg.DEEPSORT.MAX_AGE, n_init=cfg.DEEPSORT.N_INIT, nn_budget=cfg.DEEPSORT.NN_BUDGET,
                        use_cuda=True)

    min_confidence = cfg.DEEPSORT.MIN_CONFIDENCE
    nms_max_overlap = cfg.DEEPSORT.NMS_MAX_OVERLAP

    extractor = Extractor(cfg.DEEPSORT.REID_CKPT, use_cuda=True)

    max_cosine_distance = cfg.DEEPSORT.MAX_DIST
    nn_budget = 100
    metric = NearestNeighborDistanceMetric("cosine", max_cosine_distance, nn_budget)
    tracker = Tracker(metric, max_iou_distance=cfg.DEEPSORT.MAX_IOU_DISTANCE, max_age=cfg.DEEPSORT.MAX_AGE,
                      n_init=cfg.DEEPSORT.N_INIT)

    video_capture = cv2.VideoCapture("水口-检修平台下游侧.ts")

    video_fps = video_capture.get(cv2.CAP_PROP_FPS)
    w = int(video_capture.get(3))
    h = int(video_capture.get(4))
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    print(w, h, video_fps)

    command = ['ffmpeg',
               '-y',
               '-f', 'rawvideo',
               '-vcodec', 'rawvideo',
               '-pix_fmt', 'bgr24',
               '-thread_queue_size', '512',
               '-s', "{}x{}".format(w, h),
               '-r', str(video_fps),
               '-i', '-',
               '-c:v', 'libx264',
               '-pix_fmt', 'yuv420p',
               '-preset', 'ultrafast',
               '-tune', 'zerolatency',
               '-sc_threshold', '499',
               '-rtsp_transport', 'tcp',
               '-f', 'rtsp',
               rtmpUrl]

    # 管道配置
    p = sp.Popen(command, stdin=sp.PIPE)
    count = 0
    output_dict = {'person': (0, 0, 255), 'hat': (255, 0, 0)}
    while True:
        if len(stack) > 0:
            frame = stack.pop()
            image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            if count % 50 == 0:
                try:
                    xywhs, confss, classnames = model.detect_video(image)
                except Exception as e:
                    print("########")
                    continue

                bbox_tlwh = deepsort._xywh_to_tlwh(xywhs)
                features = deepsort._get_features(xywhs, image)
            else:
                for track in tracker.tracks:
                    det = torch.tensor([track.to_tlwh().tolist()], dtype=torch.float32)
                    bbox_tlwh = torch.cat([bbox_tlwh, det], dim=0) if bbox_tlwh is not None else det
                    features = deepsort._get_features(bbox_tlwh, image)
                    tempclass.append(track.cls)
                classnames = torch.Tensor(tempclass)

            detections = [Detection(bbox_tlwh[i], conf, classnames[i], features[i]) for i, conf in enumerate(confss) if
                          conf > min_confidence]

            boxes = np.array([d.tlwh for d in detections])
            scores = np.array([d.confidence for d in detections])
            indices = non_max_suppression(boxes, nms_max_overlap, scores)
            detections = [detections[i] for i in indices]

            tracker.predict()
            tracker.update(detections)

            bbox_tlwh = None
            classnames = []
            tempclass = []

            outputs = []
            for track in tracker.tracks:
                if track.time_since_update > 1:
                    continue
                box = track.to_tlwh()
                x1, y1, x2, y2 = deepsort._tlwh_to_xyxy(box)
                track_id = track.track_id
                cls = track.cls
                outputs.append(np.array([x1, y1, x2, y2, cls, track_id], dtype=np.int))
            if len(outputs) > 0:
                outputs = np.stack(outputs, axis=0)

            # outputs = deepsort.update(xywhs, confss, classnames,image)
            # print(outputs)
            bbox_xyxy = outputs[:, :5]
            # classname = outputs[:, 4]
            for box in bbox_xyxy:
                xmin, ymin, xmax, ymax, classname = box[0], box[1], box[2], box[3], box[4]
                label = model.names[int(classname)]
                cv2.rectangle(frame, (int(xmin), int(ymin)), (int(xmax), int(ymax)), output_dict[label], 4)
                cv2.putText(frame, str(label), (int(xmin), int(ymin - 10)), 0, 5e-3 * 150, output_dict[label], 3)

                # cv2.namedWindow("YOLO5_Deep_SORT", 0);
            # cv2.resizeWindow('YOLO5_Deep_SORT', w, h);
            # cv2.imshow('YOLO5_Deep_SORT', frame)
            p.stdin.write(frame.tostring())

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


if __name__ == '__main__':
    t = Manager().list()
    t1 = Process(target=receive, args=(t,))
    t2 = Process(target=realse, args=(t,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

