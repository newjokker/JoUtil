# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.txkjRes.segmentJson import SegmentJson
from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil
import base64
import numpy as np
from labelme import utils
import labelme
import cv2
from PIL import Image


a = SegmentJson()
dete_res = DeteRes()

mask = cv2.imread(r"C:\Users\14271\Desktop\test\test.png")

a.get_segment_obj_from_mask(mask[:,:,1])

a.print_as_fzc_format()

a.save_to_josn(r"C:\Users\14271\Desktop\test\test.json")

