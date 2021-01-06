# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
import copy
import random
import collections
from PIL import Image
import numpy as np
from JoTools.utils.JsonUtil import JsonUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.txkj.parseXml import parse_xml, save_to_xml
import cv2



class SegmentObj(object):
    """检测结果的一个检测对象，就是一个矩形框对应的信息"""
