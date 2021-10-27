# -*- coding: utf-8  -*-
# -*- author: jokker -*-




from lib_xjQX.detect_libs.ljjxjR2cnnDetection import ljcR2cnnDetection
from lib.detect_libs.xjdectR2cnnPytorchDetection import XjdectR2cnnDetection
from lib_xjQX.detect_libs.xjDeeplabDetection import xjDeeplabDetection
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkjRes.deteRes import DeteRes
import cv2


def parse_args():
    parser = argparse.ArgumentParser(description='Tensorflow Faster R-CNN demo')
    #
    parser.add_argument('--imgDir',dest='imgDir',type=str, default=r"/usr/input_picture")
    parser.add_argument('--modelList',dest='modelList',default="M1,M2,M3,M4,M5,M6,M7,M8,M9")
    parser.add_argument('--jsonPath',dest='jsonPath', default=r"/usr/input_picture_attach/pictureName.json")
    parser.add_argument('--outputDir',dest='outputDir', default=r"/usr/output_dir")
    #
    parser.add_argument('--scriptIndex',dest='scriptIndex', default=r"1-1")
    #
    parser.add_argument('--gpuID', dest='gpuID',type=int,default=0)
    parser.add_argument('--port',dest='port',type=int,default=45452)
    parser.add_argument('--gpuRatio',dest='gpuRatio',type=float,default=0.3)
    parser.add_argument('--host',dest='host',type=str,default='127.0.0.1')
    parser.add_argument('--logID',dest='logID',type=str,default=str(uuid.uuid1())[:6])
    parser.add_argument('--objName',dest='objName',type=str,default='')
    #
    args = parser.parse_args()
    return args


model_xjQX_1 = XjdectR2cnnDetection(args, "xjQX_ljc", scriptName)
model_xjQX_1.model_restore()



img_dir = r""

for each_img_path in FileOperationUtil.re_all_file(img_dir, endswitch=['.jpg', '.JPG']):

    xjQX_dete_res = DeteRes()

    xjQX_dete_res.img_path = each_img_path

    im = xjQX_dete_res.get_img_array(RGB=True)

    detectBoxes = model_xjQX_1.detect(im, name)
    results = model_xjQX_1.postProcess2(im, name, detectBoxes)

    print('*' * 50)
    print(detectBoxes)
    print(results)
    print('*' * 50)
