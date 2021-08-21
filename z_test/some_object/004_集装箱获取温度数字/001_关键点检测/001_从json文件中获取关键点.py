# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.segmentRes import SegmentRes, SegmentObj
from JoTools.utils.FileOperationUtil import FileOperationUtil
import numpy as np
import cv2
import os
import uuid
from JoTools.utils.CsvUtil import CsvUtil



json_dir = r"C:\Users\14271\Desktop\test_001"
save_dir = r"C:\Users\14271\Desktop\test_001_res"


csv_info = []

for each_json_path in FileOperationUtil.re_all_file(json_dir, endswitch=[".json"]):

    a = SegmentRes()
    a.parse_json_info(each_json_path, parse_img=True)

    if len(a.shapes) >1:
        shape_0, shape_1 = a.shapes[0], a.shapes[1]
        shape = shape_0 if shape_0.get_area() > shape_1.get_area() else shape_1
        #a.shapes = [shape]
        # a.crop_and_save(r"C:\Users\14271\Desktop\save_dir")

        if len(shape.points) == 4:

            add_res = np.array(list(map(lambda x:x[0] + x[1], shape.points)))
            max_index = add_res.argmax()

            if max_index == 0:
                points = shape.points
            elif max_index ==1:
                points = [shape.points[1], shape.points[2], shape.points[3], shape.points[0]]
            elif max_index == 2:
                points = [shape.points[2], shape.points[3], shape.points[0], shape.points[1]]
            elif max_index == 3:
                points = [shape.points[3], shape.points[0], shape.points[1], shape.points[2]]
            else:
                raise ValueError("* max index ∈ [0, 3]")

            # ----------------------------------------------------------------------------------------------------------
            each_uuid = str(uuid.uuid1())
            each_img_path = os.path.join(save_dir, "{0}.jpg".format(each_uuid))
            cv2.imwrite(each_img_path, a.image_data)
            each_csv_info = []
            x, y = list(zip(*points))

            print(x)
            print(y)

            each_csv_info.append(each_uuid)
            each_csv_info.extend(x)
            each_csv_info.extend(y)

            csv_info.append(each_csv_info)

CsvUtil.save_list_to_csv(csv_info, r"C:\Users\14271\Desktop\test_001_res\points.csv")











