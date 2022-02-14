# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import ctypes
import os
import random
import sys
import threading
import time

sys.path.insert(0, r"/home/tensorRT/tensorrtx/yolov5")
PLUGIN_LIBRARY = "/home/tensorRT/tensorrtx/yolov5/build/libmyplugins.so"
ctypes.CDLL(PLUGIN_LIBRARY)

import cv2
import numpy as np
import pycuda.driver as cuda
import pycuda.autoinit
import tensorrt as trt
import torch
import torchvision

# --------------------

import torch
import configparser
from ..detect_utils.log import detlog
from ..detect_utils.tryexcept import try_except
from ..detect_libs.abstractBase import detection
from ..detect_utils.cryption import salt, decrypt_file
from ..JoTools.txkjRes.deteRes import DeteRes
from ..JoTools.txkjRes.deteObj import DeteObj
from ..yolov5_libs.torch_utils import select_device



class Yolov5RT(detection):

    def __init__(self, args, objName, scriptName):
        super(Yolov5RT, self).__init__(objName, scriptName)
        # self.cfx = cuda.Device(0).make_context()
        self.readCfg()
        self.readArgs(args)
        self.log = detlog(self.modelName, self.objName, self.logID)
        self.device = select_device(str(self.gpuID))

    def readArgs(self, args):
        self.portNum = args.port
        self.gpuID = args.gpuID
        self.gpuRatio = args.gpuRatio
        self.host = args.host
        self.logID = args.logID

    # @try_except()
    def readCfg(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(self.cfgPath)
        self.modelName = self.cf.get('common', 'model')
        self.encryption = self.cf.getboolean("common", 'encryption')
        self.debug = self.cf.getboolean("common", 'debug')
        self.model_path = self.cf.get(self.objName, 'modelName')
        self.imgsz = self.cf.getint(self.objName, 'img_size')
        self.score = self.cf.getfloat(self.objName, 'conf_threshold')
        self.iou = self.cf.getfloat(self.objName, 'iou_threshold')
        self.augment = self.cf.getboolean(self.objName, 'augment')
        self.classes = [c.strip() for c in self.cf.get(self.objName, "classes").split(",")]
        self.class_dict = dict(zip(range(len(self.classes)), self.classes))
        self.visible_classes = [c.strip() for c in self.cf.get(self.objName, "visible_classes").split(",")]
        try:
            self.run_mode = self.cf.get('common', 'run_mode')
        except:
            self.run_mode = 'crop'

        self.INPUT_W = self.INPUT_H = self.imgsz
        self.CONF_THRESH = self.score
        self.IOU_THRESHOLD = self.iou

    @try_except()
    def _load_engine(self, engine_file_path):
        # Create a Context on this device,
        self.cfx = cuda.Device(0).make_context()
        stream = cuda.Stream()
        TRT_LOGGER = trt.Logger(trt.Logger.INFO)
        runtime = trt.Runtime(TRT_LOGGER)

        # Deserialize the engine from file
        with open(engine_file_path, "rb") as f:
            engine = runtime.deserialize_cuda_engine(f.read())
        context = engine.create_execution_context()

        host_inputs = []
        cuda_inputs = []
        host_outputs = []
        cuda_outputs = []
        bindings = []

        for binding in engine:
            size = trt.volume(engine.get_binding_shape(binding)) * engine.max_batch_size
            dtype = trt.nptype(engine.get_binding_dtype(binding))
            # Allocate host and device buffers
            host_mem = cuda.pagelocked_empty(size, dtype)
            cuda_mem = cuda.mem_alloc(host_mem.nbytes)
            # Append the device buffer to device bindings.
            bindings.append(int(cuda_mem))
            # Append to the appropriate list.
            if engine.binding_is_input(binding):
                host_inputs.append(host_mem)
                cuda_inputs.append(cuda_mem)
            else:
                host_outputs.append(host_mem)
                cuda_outputs.append(cuda_mem)

        # Store
        self.stream = stream
        self.context = context
        self.engine = engine
        self.host_inputs = host_inputs
        self.cuda_inputs = cuda_inputs
        self.host_outputs = host_outputs
        self.cuda_outputs = cuda_outputs
        self.bindings = bindings

    @try_except()
    def model_restore(self):

        self.log.info('===== model restore start =====')

        # 加密模型
        if self.encryption:
            model_path = self.dncryptionModel()
        else:
            model_path = os.path.join(self.modelPath, self.model_path)
        print("self.encryption:", self.encryption)
        print(model_path)

        self._load_engine(model_path)
        self.warmUp()
        self.log.info("load complete")
        print("load complete")

        # 删除解密的模型
        if self.encryption:
            os.remove(model_path)
            self.log.info('delete dncryption model successfully! ')

    # @try_except()
    def detectSOUT(self, path=None, image=None, image_name="default.jpg"):
        if path == None and image is None:
            raise ValueError("path and image cannot be both None")

        dete_res = DeteRes()
        dete_res.img_path = path
        dete_res.file_name = image_name

        # Make self the active context, pushing it on top of the context stack.
        if self.cfx:
            self.cfx.push()
        # Restore
        stream = self.stream
        context = self.context
        engine = self.engine
        host_inputs = self.host_inputs
        cuda_inputs = self.cuda_inputs
        host_outputs = self.host_outputs
        cuda_outputs = self.cuda_outputs
        bindings = self.bindings
        # Do image preprocess
        if path is not None:
            input_image, origin_h, origin_w = self.preprocess_image(path=path)
        else:
            input_image, origin_h, origin_w = self.preprocess_image(image=image)
        # Copy input image to host buffer
        np.copyto(host_inputs[0], input_image.ravel())
        # Transfer input data  to the GPU.
        cuda.memcpy_htod_async(cuda_inputs[0], host_inputs[0], stream)
        # Run inference.
        context.execute_async(bindings=bindings, stream_handle=stream.handle)
        # Transfer predictions back from the GPU.
        cuda.memcpy_dtoh_async(host_outputs[0], cuda_outputs[0], stream)
        # Synchronize the stream
        stream.synchronize()
        # Remove any context from the top of the context stack, deactivating it.
        if self.cfx:
            self.cfx.pop()
        # Here we use the first row of output in that batch_size = 1
        output = host_outputs[0]
        # Do postprocess
        boxes, scores, classes = self.post_process(
            output, origin_h, origin_w
        )
        boxes = boxes.cpu().numpy()
        scores = scores.cpu().numpy()
        classes = classes.cpu().numpy()

        for i in range(len(boxes)):
            xmin, ymin, xmax, ymax = boxes[i]
            # print(classes[i])
            label = self.class_dict[classes[i]]
            prob = float(scores[i])
            dete_obj = DeteObj(x1=int(xmin), y1=int(ymin), x2=int(xmax), y2=int(ymax), tag=label, conf=prob, assign_id=i)
            dete_res.add_obj_2(dete_obj)
        return dete_res

    @try_except()
    def destroy(self):
        # Remove any context from the top of the context stack, deactivating it.
        self.cfx.pop()

    @try_except()
    def preprocess_image(self, path=None, image=None):
        """
        description: Read an image from image path, convert it to RGB,
                     resize and pad it to target size, normalize to [0,1],
                     transform to NCHW format.
        param:
            input_image_path: str, image path
        return:
            image:  the processed image
            image_raw: the original image
            h: original height
            w: original width
        """

        if path is not None:
            image_raw = cv2.imdecode(np.fromfile(path, dtype=np.uint8), 1)
            image = cv2.cvtColor(image_raw, cv2.COLOR_BGR2RGB)
        else:
            image = image

        h, w, c = image.shape
        # Calculate widht and height and paddings
        r_w = self.INPUT_W / w
        r_h = self.INPUT_H / h
        if r_h > r_w:
            tw = self.INPUT_W
            th = int(r_w * h)
            tx1 = tx2 = 0
            ty1 = int((self.INPUT_H - th) / 2)
            ty2 = self.INPUT_H - th - ty1
        else:
            tw = int(r_h * w)
            th = self.INPUT_H
            tx1 = int((self.INPUT_W - tw) / 2)
            tx2 = self.INPUT_W - tw - tx1
            ty1 = ty2 = 0
        # Resize the image with long side while maintaining ratio
        image = cv2.resize(image, (tw, th))
        # Pad the short side with (128,128,128)
        image = cv2.copyMakeBorder(
            image, ty1, ty2, tx1, tx2, cv2.BORDER_CONSTANT, (128, 128, 128)
        )
        image = image.astype(np.float32)
        # Normalize to [0,1]
        image /= 255.0
        # HWC to CHW format:
        image = np.transpose(image, [2, 0, 1])
        # CHW to NCHW format
        image = np.expand_dims(image, axis=0)
        # Convert the image to row-major order, also known as "C order":
        image = np.ascontiguousarray(image)
        return image, h, w

    def _xywh2xyxy(self, origin_h, origin_w, x):
        """
        description:    Convert nx4 boxes from [x, y, w, h] to [x1, y1, x2, y2] where xy1=top-left, xy2=bottom-right
        param:
            origin_h:   height of original image
            origin_w:   width of original image
            x:          A boxes tensor, each row is a box [center_x, center_y, w, h]
        return:
            y:          A boxes tensor, each row is a box [x1, y1, x2, y2]
        """
        y = torch.zeros_like(x) if isinstance(x, torch.Tensor) else np.zeros_like(x)
        r_w = self.INPUT_W / origin_w
        r_h = self.INPUT_H / origin_h
        if r_h > r_w:
            y[:, 0] = x[:, 0] - x[:, 2] / 2
            y[:, 2] = x[:, 0] + x[:, 2] / 2
            y[:, 1] = x[:, 1] - x[:, 3] / 2 - (self.INPUT_H - r_w * origin_h) / 2
            y[:, 3] = x[:, 1] + x[:, 3] / 2 - (self.INPUT_H - r_w * origin_h) / 2
            y /= r_w
        else:
            y[:, 0] = x[:, 0] - x[:, 2] / 2 - (self.INPUT_W - r_h * origin_w) / 2
            y[:, 2] = x[:, 0] + x[:, 2] / 2 - (self.INPUT_W - r_h * origin_w) / 2
            y[:, 1] = x[:, 1] - x[:, 3] / 2
            y[:, 3] = x[:, 1] + x[:, 3] / 2
            y /= r_h

        return y

    @try_except()
    def post_process(self, output, origin_h, origin_w):
        """
        description: postprocess the prediction
        param:
            output:     A tensor likes [num_boxes,cx,cy,w,h,conf,cls_id, cx,cy,w,h,conf,cls_id, ...]
            origin_h:   height of original image
            origin_w:   width of original image
        return:
            result_boxes: finally boxes, a boxes tensor, each row is a box [x1, y1, x2, y2]
            result_scores: finally scores, a tensor, each element is the score correspoing to box
            result_classid: finally classid, a tensor, each element is the classid correspoing to box
        """
        # Get the num of boxes detected
        num = int(output[0])
        # Reshape to a two dimentional ndarray
        pred = np.reshape(output[1:], (-1, 6))[:num, :]
        # to a torch Tensor
        pred = torch.Tensor(pred).cuda()
        # Get the boxes
        boxes = pred[:, :4]
        # Get the scores
        scores = pred[:, 4]
        # Get the classid
        classid = pred[:, 5]
        # Choose those boxes that score > CONF_THRESH
        si = scores > self.CONF_THRESH
        boxes = boxes[si, :]
        scores = scores[si]
        classid = classid[si]
        # Trandform bbox from [center_x, center_y, w, h] to [x1, y1, x2, y2]
        boxes = self._xywh2xyxy(origin_h, origin_w, boxes)
        # Do nms
        indices = torchvision.ops.nms(boxes, scores, iou_threshold=self.IOU_THRESHOLD).cpu()
        result_boxes = boxes[indices, :].cpu()
        result_scores = scores[indices].cpu()
        result_classid = classid[indices].cpu()
        return result_boxes, result_scores, result_classid

    # ------------------------------------------------------------------------------------------------------------------

    @try_except()
    def warmUp(self):
        res = self.detectSOUT(image=np.zeros((640,640,3), dtype=np.uint8))
        print(res)
        print("* warm up success")

    @try_except()
    def dncryptionModel(self):
        if not os.path.exists(self.cachePath):
            os.makedirs(self.cachePath)

        # 解密模型
        name, ext = os.path.splitext(self.model_path)
        model_origin_name = name + ext
        model_locked_name = name + "_locked" + ext
        origin_Fmodel = os.path.join(self.cachePath, model_origin_name)
        locked_Fmodel = os.path.join(self.modelPath, model_locked_name)
        decrypt_file(salt, locked_Fmodel, origin_Fmodel)

        # 解密后的模型
        tfmodel = os.path.join(self.cachePath, self.model_path)
        return tfmodel


