#-*- coding: UTF-8 -*-  
#!/usr/bin/env python

# --------------------------------------------------------
# Tensorflow Faster R-CNN
# Licensed under The MIT License [see LICENSE for details]
# Written by Xinlei Chen, based on code from Ross Girshick
# --------------------------------------------------------

import os, sys
this_dir = os.path.dirname(__file__)
lib_path = os.path.join(this_dir, '..')
sys.path.insert(0, lib_path)
import argparse
import cv2
import json
import torch
import numpy as np
import threading
from PIL import Image
import uuid

from lib.detect_libs.yolov5Detection import YOLOV5Detection
from lib.detect_utils.timer import Timer
from lib.detect_libs.fasterDetectionPyTorch import FasterDetectionPytorch
from lib.detect_libs.vggClassify import VggClassify
from lib.detect_libs.clsDetectionPyTorch import ClsDetectionPyTorch
from lib.detect_libs.ljcY5Detection import LjcDetection
from lib.detect_libs.kkgY5Detection import KkgDetection
from lib.detect_libs.clsDetectionPyTorch import ClsDetectionPyTorch
from lib_xjQX.detect_libs.ljjxjR2cnnDetection import ljcR2cnnDetection
from lib_xjQX.detect_libs.xjDeeplabDetection import xjDeeplabDetection
#
from lib.JoTools.txkjRes.resTools import ResTools
from lib.JoTools.utils.FileOperationUtil import FileOperationUtil
from lib.JoTools.utils.CsvUtil import CsvUtil
from lib.JoTools.txkjRes.deteRes import DeteRes
from lib.JoTools.txkjRes.deteObj import DeteObj
from lib.JoTools.txkjRes.deteAngleObj import DeteAngleObj
from lib.JoTools.utils.JsonUtil import JsonUtil


M_dict = {
    "M1":"杆塔类",
    "M2":"导地线类",
    "M3":"绝缘子类",
    "M4":"大尺寸金具类",
    "M5":"小尺寸金具类",
    "M6":"基础类",
    "M7":"通道环境类",
    "M8":"接地装置类",
    "M9":"附属设施类"
}

M_model_list ={
    "M1":["nc"],
    "M2":[],
    "M3":["jyzZB", "jyzQX"],
    "M4":["fzc", "fzcRust", "xjQX", "jyhQX", "ljcRust"],
    "M5":["kkxQuiting", "kkxTC", "kkxRust"],
    "M6":[],
    "M7":["waipo"],
    "M8":[],
    "M9":["fncDK"],
}

key_M_dict = {
    "杆塔":"M1",
    "导地线":"M2",
    "绝缘子":"M3",
    "大金具":"M4",
    "小金具":"M5",
    "基础":"M6",
    "通道环境":"M7",
    "接地装置":"M8",
    "附属设施":"M9",
}

tag_code_dict = {

    # --------------------------------------------------------------------------------------------------------------
    # 开口销缺失
    "K": "040500013",

    # 开口销缺失
    "kkxTC": "040500023",

    # 安装不规范
    "illegal": "040500023",

    # 销钉锈蚀
    "K_KG_rust": "040500033",

    # 螺母锈蚀
    "Lm_rust": "040501013",
    # --------------------------------------------------------------------------------------------------------------

    # 鸟巢蜂巢
    "nc": "010000021",
    "fw": "010000021",

    # 玻璃绝缘子自爆
    "jyzzb": "030100023",

    # 绝缘子污秽
    "abnormal": "030100011",

    # 均压环倾斜
    "fail": "030200131",

    # 金具锈蚀
    "rust": "040000011",

    # 防振锤锈蚀
    "fzc_rust": "040303031",

    # 防振锤破损
    "fzc_broken": "040303021",

    "sg": "040402011",

    # --------------------------------------------------------------------------------------------------------------
    # 吊塔
    "TowerCrane": "060800013",

    # 推土机
    "Bulldozer": "060800023",

    # 挖掘机
    "Digger": "060800033",

    "CementPumpTruck_yb": "060800033",
    # --------------------------------------------------------------------------------------------------------------

    # 线夹缺垫片
    "dp_missed": "040001042",

    # 线夹缺倾斜
    "XJfail": "040000071",

    # 防鸟刺安装不规范
    "fncBGF": "070400031",

    # 防鸟刺未打开
    "weidakai": "070400021",

    # jiedi
    "050000011": "050000011",
    "050001012": "050001012",

    # jichu
    "000000181": "000000051",
    "000000151": "000000151",
    "000000081": "000000081",
    "000000051": "000000051",
}


def xml_to_csv(xml_dir, csv_save_path):
    """将保存的 xml 文件信息存放在 csv 文件中"""
    csv_list = [['filename', 'code', 'score', 'xmin', 'ymin', 'xmax', 'ymax']]


    CsvUtil.save_list_to_csv(csv_list, csv_save_path)


class SaveLog():

    def __init__(self, log_path, img_count, csv_path=None):
        self.log_path = log_path
        self.img_count = img_count
        self.img_index = 1
        self.csv_path = csv_path
        self.csv_list = [['filename', 'name', 'score', 'xmin', 'ymin', 'xmax', 'ymax']]
        # empty log
        if os.path.exists(self.log_path):
            os.remove(self.log_path)

    def add_log(self, img_name):
        self.log = open(self.log_path, 'a')
        self.log.write("process:{0}/{1} {2}\n".format(self.img_index, self.img_count, img_name))
        self.img_index += 1
        self.log.close()

    def add_csv_info(self, dete_res, img_name):
        #
        for dete_obj in dete_res:
            if dete_obj.tag in tag_code_dict:
                each_code = tag_code_dict[dete_obj.tag]
                self.csv_list.append([img_name, each_code, dete_obj.conf, dete_obj.x1, dete_obj.y1, dete_obj.x2, dete_obj.y2])

    def read_img_list_finshed(self):
        self.log = open(self.log_path, 'a')
        self.log.write("Loading Finished\n")
        self.log.close()

    def close(self):
        self.log = open(self.log_path, 'a')
        self.log.write("---process complete---\n")
        self.log.close()
        # save csv
        CsvUtil.save_list_to_csv(self.csv_list, self.csv_path)


def parse_args():
    parser = argparse.ArgumentParser(description='Tensorflow Faster R-CNN demo')
    #
    parser.add_argument('--imgDir',dest='imgDir',type=str, default=r"/usr/input_picture")
    parser.add_argument('--modelList',dest='modelList',default="M1,M2,M3,M4,M5,M6,M7,M8,M9")
    parser.add_argument('--jsonPath',dest='jsonPath', default=r"/usr/input_picture_attach/pictureName.json")
    parser.add_argument('--outputDir',dest='outputDir', default=r"/usr/output_dir")
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


def get_json_dict(json_path):
    img_name_json_dict = {}
    #
    name_info = JsonUtil.load_data_from_json_file(json_path)
    for each in name_info:
        img_name_json_dict[each["originFileName"]] = each["fileName"]
        #img_name_json_dict[each["fileName"]] = each["originFileName"]
    return img_name_json_dict


def screen(y, img):
    #screen brightness
    _, _, v = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))
    vmedian = np.median(v)
    if vmedian < 35:
        y='0'
    #screen obscure
    blurry=cv2.Laplacian(img,cv2.CV_64F).var()
    if blurry<200:
        y='0'
    return y


def get_model_list_from_img_name(img_name, M_list):
    """从文件名中获取 model_list，传入的是文件名不是完整的路径"""

    model_set = set()
    is_empty = True
    for each_key in key_M_dict:
    # for each_key in key_M_dict:
        if each_key in img_name:
            is_empty = False
            if key_M_dict[each_key] in M_list:
                for each_model_name in M_model_list[key_M_dict[each_key]]:
                    model_set.add(each_model_name)
    if len(model_set) > 0:
        return list(model_set)
    elif is_empty:
        # 模型名真的不带要检测的关键字信息
        # 解析不到文件名中的关键字的，用能使用的所有模型
        for key in M_list:
            for each_model_name in M_model_list[key]:
                model_set.add(each_model_name)
        return model_set
    else:
        return model_set


def model_restore(args, scriptName, model_list=None):
    """模型预热"""
    
    model_dict = {}
    
    if model_list is None:
        model_list = ['nc' ,'jyzZB', 'fzc', 'fzcRust', 'ljcRust', 'fncDK', 'kkxTC', 'kkxQuiting', 'kkxRust', 'waipo', 'xjQX']
    
     
    if "xjQX" in model_list:
        model_xjQX_1 = ljcR2cnnDetection(args, "ljjxj", scriptName)
        model_xjQX_1.model_restore()
        model_xjQX_2 = xjDeeplabDetection(args, "xj_deeplab", scriptName)
        model_xjQX_2.model_restore()
        model_dict["model_xjQX_1"] = model_xjQX_1
        model_dict["model_xjQX_2"] = model_xjQX_2
        
    if "jyzZB" in model_list:
        model_jyzZB_1 = YOLOV5Detection(args, "jyz", scriptName)
        model_jyzZB_1.model_restore()
        model_jyzZB_2 = YOLOV5Detection(args, "jyzzb", scriptName)
        model_jyzZB_2.model_restore()
        model_dict["model_jyzZB_1"] = model_jyzZB_1
        model_dict["model_jyzZB_2"] = model_jyzZB_2
       
    
    if "nc" in model_list:
        model_nc = YOLOV5Detection(args, "nc", scriptName)
        model_nc.model_restore()
        model_dict["model_nc"] = model_nc

    if "fzc" in model_list:
        model_fzc_1 = FasterDetectionPytorch(args,"fzc_step_one", scriptName)
        model_fzc_1.model_restore()
        model_fzc_2 = VggClassify(args,"fzc_step_new", scriptName)
        model_fzc_2.model_restore()
        model_dict["model_fzc_1"] = model_fzc_1
        model_dict["model_fzc_2"] = model_fzc_2
        
        
    if "fzcRust" in model_list:
        model_fzc_rust = ClsDetectionPyTorch(args, "fzc_rust", scriptName)
        model_fzc_rust.model_restore()
        model_dict["model_fzc_rust"] = model_fzc_rust
    
    
    if "fncDK" in model_list:
        model_fnc = YOLOV5Detection(args, "fnc", scriptName)
        model_fnc.model_restore()
        model_dict["model_fnc"] = model_fnc
        
        
    if "kkxTC" in model_list or "kkxQuiting" in model_list or "kkxRust" in model_list:
        model_kkxTC_1 = LjcDetection(args, "kkxTC_ljc", scriptName)
        model_kkxTC_1.model_restore()
        model_kkxTC_2 = KkgDetection(args, "kkxTC_kkx", scriptName)
        model_kkxTC_2.model_restore()
        model_kkxTC_3 = ClsDetectionPyTorch(args, "kkxTC_lm_cls", scriptName)
        model_kkxTC_3.model_restore()
        model_kkxQuiting = ClsDetectionPyTorch(args, "kkxQuiting_cls", scriptName)
        model_kkxQuiting.model_restore()
        model_kkxRust = VggClassify(args, "kkxRust", scriptName)
        model_kkxRust.model_restore()
        model_dict["model_kkxTC_1"] = model_kkxTC_1
        model_dict["model_kkxTC_2"] = model_kkxTC_2
        model_dict["model_kkxTC_3"] = model_kkxTC_3
        model_dict["model_kkxQuiting"] = model_kkxQuiting
        model_dict["model_kkxRust"] = model_kkxRust

    if "waipo" in model_list:
        model_waipo = YOLOV5Detection(args, "waipo", scriptName)
        model_waipo.model_restore()
        model_dict["model_waipo"] = model_waipo
        
    if "ljcRust" in model_list:
        model_ljc_rust_1 = YOLOV5Detection(args, "ljc_rust_one", scriptName)
        model_ljc_rust_1.model_restore()
        model_ljc_rust_2 = ClsDetectionPyTorch(args, "ljc_rust_two", scriptName)    
        model_ljc_rust_2.model_restore()
        model_dict["model_ljc_rust_1"] = model_ljc_rust_1
        model_dict["model_ljc_rust_2"] = model_ljc_rust_2

    return model_dict


def model_dete(img_path, model_dict, model_list=None):
    """进行模型检测"""

    name = os.path.split(img_path)[1]

    if model_list is None:
        model_list = ['nc' ,'jyzZB', 'fzc', 'fzcRust', 'ljcRust', 'fncDK', 'kkxTC', 'kkxQuiting', 'kkxRust', 'waipo', 'xjQX']

    # im
    data = {"path": img_path}
    im = np.array(Image.open(data['path']))
    
    # dete result for all
    dete_res_all = DeteRes()
    dete_res_all.img_path = img_path
          
    
    if "jyzZB" in model_list:
    
        if ("model_jyzZB_1" not in model_dict):
            print("* error : no model : model_jyzZB_1") 
            
            
        if ("model_jyzZB_2" not in model_dict):
            print("* error : no model : model_jyzZB_2")

        try:
            model_jyzZB_1 = model_dict["model_jyzZB_1"]
            model_jyzZB_2 = model_dict["model_jyzZB_2"]

            # jyzZB step_1
            dete_res_jyzZB = model_jyzZB_1.detectSOUT(path=data['path'], image_name=name)
            #torch.cuda.empty_cache()
            # ---------------------------------------
            # jyzZB step_2     
            result_res = DeteRes(assign_img_path=data['path'])
            result_res.img_path = data['path']
            # 
            result_res.file_name = name
            for each_dete_obj in dete_res_jyzZB:
                each_dete_obj.do_augment([150,150,150,150],dete_res_jyzZB.width,dete_res_jyzZB.height,is_relative=False)
                each_im = dete_res_jyzZB.get_sub_img_by_dete_obj(each_dete_obj)
                new_dete_res = model_jyzZB_2.detectSOUT(image = each_im,image_name = each_dete_obj.get_name_str())
                new_dete_res.offset(each_dete_obj.x1, each_dete_obj.y1)
                result_res += new_dete_res
            #MYLOG.info(result_res.get_fzc_format())
            result_res.do_nms_center_point(ignore_tag=True)
            result_res.update_tags({"jyzSingle":"jyzzb"}) 
            dete_res_all += result_res
            #torch.cuda.empty_cache()
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])
            print(e.__traceback__.tb_lineno)
        
    if "nc" in model_list:
    
        if ("model_nc" not in model_dict):
            print("* error : no model : model_nc")
    
        try:

            model_nc = model_dict["model_nc"]

            nc_dete_res = model_nc.detectSOUT(path=data['path'], image_name=name)
            dete_res_all += nc_dete_res
            #torch.cuda.empty_cache()
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])
            print(e.__traceback__.tb_lineno)
                
    if "waipo" in model_list:
    
        if ("model_waipo" not in model_dict):
            print("* error : no model : model_waipo")
    
        try:

            model_waipo = model_dict["model_waipo"]

            waipo_dete_res = model_waipo.detectSOUT(path=data['path'], image_name=name)
            dete_res_all += waipo_dete_res
            #torch.cuda.empty_cache()
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])
            print(e.__traceback__.tb_lineno)
    
    if "fzc" in model_list:

        if ("model_fzc_1" not in model_dict):
            print("* error : no model : model_fzc_1")
            
        if ("model_fzc_2" not in model_dict):
            print("* error : no model : model_fzc_2")
            
        if ("model_fzc_rust" not in model_dict):
            print("* error : no model : model_fzc_rust")
        
    
        try:

            model_fzc_1 = model_dict["model_fzc_1"]
            model_fzc_2 = model_dict["model_fzc_2"]
            model_fzc_rust = model_dict["model_fzc_rust"]

            # step_1 
            dete_res_fzc = model_fzc_1.detectSOUT(path=data['path'], image_name=name)
            # step_2
            for each_dete_obj in dete_res_fzc:
                crop_array = dete_res_fzc.get_sub_img_by_dete_obj(each_dete_obj, RGB=False, augment_parameter=[0.1, 0.1, 0.1, 0.1])
                new_label, conf = model_fzc_2.detect_new(crop_array, name)
                # 
                each_dete_obj.tag = new_label
                each_dete_obj.conf = conf
                # 
                if each_dete_obj.tag == "fzc_broken":
                    if each_dete_obj.conf > 0.9:
                        each_dete_obj.tag = "fzc_broken"
                    else:
                        each_dete_obj.tag = "other_fzc_broken"
                elif each_dete_obj.tag == "other":
                    each_dete_obj.tag = "other_other"
                else:
                    if each_dete_obj.conf > 0.6:
                        each_dete_obj.tag = "Fnormal"
                    else:
                        each_dete_obj.tag = "other_Fnormal"
                #        
                dete_res_all.add_obj_2(each_dete_obj)
                # rust
                if each_dete_obj.tag in ["fzc_broken", "Fnormal"]:
                    crop_array_rust = dete_res_fzc.get_sub_img_by_dete_obj(each_dete_obj, RGB=False)
                    rust_index, rust_f = model_fzc_rust.detect(crop_array_rust)
                    rust_label = ["fzc_normal","fzc_rust"][int(rust_index)]
                    rust_f = float(rust_f)
                    # 
                    each_dete_rust = each_dete_obj.deep_copy()
                    each_dete_rust.tag = rust_label
                    # 
                    dete_res_all.add_obj_2(each_dete_rust)
            #torch.cuda.empty_cache()    
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])
            print(e.__traceback__.tb_lineno)

    if "fncDK" in model_list:
    
        if ("model_fnc" not in model_dict):
            print("* error : no model : model_fnc")
    
    
        try:

            model_fnc = model_dict["model_fzc_1"]

            dete_res_fnc = model_fnc.detectSOUT(path=data['path'], image_name=name)        
            dete_res_all += dete_res_fnc
            #torch.cuda.empty_cache()
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])
            print(e.__traceback__.tb_lineno)
         
    if "kkxTC" in model_list or "kkxQuiting" in model_list or "kkxRust" in model_list:

        if ("model_kkxTC_1" not in model_dict):
            print("* error : no model : model_kkxTC_1")
            
        if ("model_kkxTC_2" not in model_dict):
            print("* error : no model : model_kkxTC_2")
            
        if ("model_kkxTC_3" not in model_dict):
            print("* error : no model : model_kkxTC_3")
            
        if ("model_kkxRust" not in model_dict):
            print("* error : no model : model_kkxRust")
            
        if ("model_kkxQuiting" not in model_dict):
            print("* error : no model : model_kkxQuiting")

        try:

            model_kkxTC_1 = model_dict["model_kkxTC_1"]
            model_kkxTC_2 = model_dict["model_kkxTC_2"]
            model_kkxTC_3 = model_dict["model_kkxTC_3"]
            model_kkxRust = model_dict["model_kkxRust"]
            model_kkxQuiting = model_dict["model_kkxQuiting"]

            # kkxTC_1
            kkxTC_1_out = model_kkxTC_1.detect(im, name)
            if len(kkxTC_1_out[0]) > 0:
                voc_labels = model_kkxTC_1.post_process(*kkxTC_1_out)
                # MYLOG.info("detect result:", voc_labels)
                kkxTC_1_results = model_kkxTC_1.postProcess2(im, *kkxTC_1_out)
            else:
                kkxTC_1_results = [] 
            # 
            kkxTC_1_dete_res = DeteRes()
            kkxTC_1_dete_res.img_path = data['path']
            for i, each_res in enumerate(kkxTC_1_results):
                label, score, [xmin, ymin, xmax, ymax] = each_res
                ljc_resizedName = name+'_'+label+'_'+str(i)+'.jpg'
                # add up_right obj
                kkxTC_1_dete_res.add_obj(int(xmin), int(ymin), int(xmax), int(ymax), str(label), conf=-1, assign_id=i, describe=ljc_resizedName)
            # 
            kkxTC_1_dete_res.do_nms(0.3)
            kkxTC_1_save_dir = model_kkxTC_1.resizedImgPath
            kkxTC_1_dete_res.crop_dete_obj(kkxTC_1_save_dir)
            # ---------------------------------------
            # kkxTC_2
            ###  单连接件 ###
            kkxTC_2_dete_kg_lm = kkxTC_1_dete_res.deep_copy(copy_img=False)
            kkxTC_2_dete_kg_lm.reset_alarms([])

            # 遍历每一个连接件正框
            for each_dete_obj in kkxTC_1_dete_res.alarms:
                each_dete_kg_lm = kkxTC_1_dete_res.deep_copy(copy_img=False)
                each_dete_kg_lm.reset_alarms([])
                # get array 连接件正框图片矩阵 np.array
                #each_sub_array = kkxTC_1_dete_res.get_sub_img_by_dete_obj(each_dete_obj,RGB=True)
                each_sub_array = kkxTC_1_dete_res.get_sub_img_by_dete_obj_from_crop(each_dete_obj, RGB=False)
                # 小金具定位检测结果集合 on a ljc martrix-cap
                kkxTC_2_out = model_kkxTC_2.detect(each_sub_array, name)
                if len(kkxTC_2_out[0]) > 0:
                    voc_labels = model_kkxTC_2.post_process(*kkxTC_2_out)
                    ## 过滤最小尺寸 ##
                    voc_labels = model_kkxTC_2.checkDetectBoxAreas(voc_labels)

                    for each_obj in voc_labels:
                        ## label, i, xmin, ymin, xmax, ymax,p
                        new_dete_obj = DeteObj(each_obj[2], each_obj[3], each_obj[4], each_obj[5], tag=each_obj[0], conf=float(each_obj[6]), assign_id=each_dete_obj.id)
                        each_dete_kg_lm.add_obj_2(new_dete_obj)

                    ## +xmap +ymap 坐标还原至原图
                    each_dete_kg_lm.offset(each_dete_obj.x1, each_dete_obj.y1)
                    # merge
                    kkxTC_2_dete_kg_lm += each_dete_kg_lm


            # 业务逻辑：other* 和 dense内的K过滤
            kkxTC_2_dete_res = kkxTC_2_dete_kg_lm.deep_copy(copy_img=False)
            only_other_3 = kkxTC_2_dete_kg_lm.deep_copy(copy_img=False)
            only_k = kkxTC_2_dete_kg_lm.deep_copy(copy_img=False)
            only_other_3.filter_by_tags(need_tag = model_kkxTC_2.labeles_checkedOut)
            only_k.filter_by_tags(need_tag=['K'])
            kkxTC_2_dete_res.filter_by_tags(remove_tag=['K'])
            # 
            for each_dete_obj in only_k:
                is_in = False
                for each_dete_obj_2 in only_other_3:
                    each_iou = ResTools.polygon_iou_1(each_dete_obj.get_points(),each_dete_obj_2.get_points()) ##
                    #print('--other* iou-->{} ,other*:{}, K: {}'.format(each_iou,each_dete_obj_2.get_points(),each_dete_obj.get_points()))
                    if each_iou > 0.8:
                        is_in = True
                if not is_in:
                    kkxTC_2_dete_res.add_obj_2(each_dete_obj)
            # 
            kkxTC_2_dete_res.do_nms(0.3)
            # 删除裁剪的小图
            kkxTC_1_dete_res.del_sub_img_from_crop()
            # ---------------------------------------
            # kkxTC_3 | kkxQuiting | kkxRust
            kkxTC_dete_res = DeteRes()
            kkxQuiting_dete_res = DeteRes()
            kkxRust_dete_res = DeteRes()
            # 
            for each_dete_obj in kkxTC_2_dete_res:
                if each_dete_obj.tag not in ['K', 'KG', 'Lm','K2', 'KG2']:
                    continue
                # 
                each_im = kkxTC_2_dete_res.get_sub_img_by_dete_obj(each_dete_obj)
                # -----------------
                # kkxTC
                # if "kkxTC" in model_list:                
                label, prob = model_kkxTC_3.detect(each_im, 'resizedName')
                each_dete_obj.conf = float(prob)
                each_dete_obj.des = each_dete_obj.tag

                if label == '2' or each_dete_obj.tag=='Lm':
                    each_dete_obj.tag = 'Lm'

                elif label == '1' and prob > model_kkxTC_3.confThresh:
                    each_dete_obj.tag = 'K'
                else:
                    each_dete_obj.tag = 'Xnormal'
                kkxTC_dete_res.add_obj_2(each_dete_obj)
                # -----------------
                # kkxRust
                if "kkxRust" in model_list:   
                    new_label, conf = model_kkxRust.detect_new(each_im, name)
                    new_dete_obj_rust = each_dete_obj.deep_copy()
                    if new_label == 'kkx_rust' and conf > 0.8:
                        if each_dete_obj.tag in ["Lm"]:
                            new_dete_obj_rust.tag = 'Lm_rust'
                        else:
                            new_dete_obj_rust.tag = 'K_KG_rust'
                    else:
                        new_dete_obj_rust.tag = 'Lnormal'
                    kkxRust_dete_res.add_obj_2(new_dete_obj_rust)
                # -----------------
                # kkxQuiting
                if "kkxQuiting" in model_list:
                    # 0:销脚可见 1:退出 2:销头销脚正对
                    if each_dete_obj.tag in ["Xnormal"]:
                        label, prob = model_kkxQuiting.detect(each_im, 'resizedName')
                        if label == '1' and prob > 0.5:
                            new_dete_obj = each_dete_obj.deep_copy()
                            new_dete_obj.tag = 'kkxTC'
                            kkxQuiting_dete_res.add_obj_2(new_dete_obj)                            
                
            if "kkxTC" in model_list:
                dete_res_all += kkxTC_dete_res
                
            if "kkxQuiting" in model_list:
                dete_res_all += kkxQuiting_dete_res
                
            if "kkxRust" in model_list:
                dete_res_all += kkxRust_dete_res
            #torch.cuda.empty_cache()
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])
            print(e.__traceback__.tb_lineno)

    if "ljcRust" in model_list:
    
        if ("model_ljc_rust_1" not in model_dict):
            print("* error : no model : model_ljc_rust_1")
            
        if ("model_ljc_rust_2" not in model_dict):
            print("* error : no model : model_ljc_rust_2")

        try:

            model_ljc_rust_1 = model_dict["model_ljc_rust_1"]
            model_ljc_rust_2 = model_dict["model_ljc_rust_2"]

            # ljc rust 1
            dete_res_ljc = model_ljc_rust_1.detectSOUT(path=data['path'], image_name=name)
            #print("ljc rust 001 start")
            dete_res_ljc.print_as_fzc_format()
            #print("ljc rust 001 end")
            dete_res_ljc.do_nms(0.3, ignore_tag=True)
            #kkxTC_1_save_dir = model_kkxTC_1.resizedImgPath
            #dete_res_ljc.crop_dete_obj(kkxTC_1_save_dir)
            
            # ---------------------------------------
            # ljc rust 2
            for each_dete_obj in dete_res_ljc:
                each_im = dete_res_ljc.get_sub_img_by_dete_obj(each_dete_obj)
                tag, conf = model_ljc_rust_2.detect(each_im)
                # logic
                # fixme screen ???
                tag = screen(tag, each_im)
                # rust : 1, normal : 0
                if (tag == '1') and (conf < 0.8):
                    tag = 'normal'
                    conf = 1 - conf
                elif tag == '1':
                    tag = 'rust'
                else:
                    tag = 'normal'
                # tag:ljj type , des:if rust
                each_dete_obj.tag = tag
                each_dete_obj.conf = conf
            # 
            dete_res_all += dete_res_ljc            
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])
            print(e.__traceback__.tb_lineno)
    
    if "xjQX" in model_list:
     
        if ("model_xjQX_1" not in model_dict):
            print("* error : no model : model_xjQX_1")
            
        if ("model_xjQX_2" not in model_dict):
            print("* error : no model : model_xjQX_2")

        try:

            model_xjQX_1 = model_dict["model_xjQX_1"]
            model_xjQX_2 = model_dict["model_xjQX_2"]


            xjQX_dete_res = DeteRes()
            #xjQX_dete_res.img_path = data['path']

            detectBoxes = model_xjQX_1.detect(im, name)
            results = model_xjQX_1.postProcess(im, name, detectBoxes)
            
            # 
            for xjBox in results:
                resizedName = xjBox['resizedName']
                resizedImg = im[xjBox['ymin']:xjBox['ymax'],xjBox['xmin']:xjBox['xmax']]
                segImage = model_xjQX_2.detect(resizedImg,resizedName)
                result = model_xjQX_2.postProcess(segImage,resizedName,xjBox)
                
                # add obj
                if "position" in result:
                    x1, y1, w, h = result["position"]
                    x2, y2 = x1 + w, y1 + h
                    tag = result["class"]
                    xjQX_dete_res.add_obj(x1, y1, x2, y2, tag, conf=-1, assign_id=-1, describe='')
                    
            dete_res_all += xjQX_dete_res
            #torch.cuda.empty_cache()
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])
            print(e.__traceback__.tb_lineno)
        

    # print
    #dete_res_all.print_as_fzc_format()

    save_dir = r"/home/suanfa-3/ldq/modelManageNewTest/testdir/modeldata/allMerge/v0.0.1_fangtian_mode_2/scripts/res"
    each_save_name = os.path.split(img_path)[1]
    each_save_path = os.path.join(save_dir, each_save_name)
    each_save_path_xml = os.path.join(save_dir, each_save_name[:-4] + '.xml')
    dete_res_all.draw_dete_res(each_save_path)
    dete_res_all.save_to_xml(each_save_path_xml)

    # empty cache
    torch.cuda.empty_cache()
    
    return dete_res_all



if __name__ == '__main__':

    args = parse_args()

    # input: (1) model_list (str)

    # output (1) csv, log  | programe.log

    # fixme 同一个位置只能输出一个框，按照重要性进行排序
    
    # ---------------------------
    img_dir = args.imgDir.strip()
    json_path = args.jsonPath
    output_dir = args.outputDir.strip()
    log_path = os.path.join(output_dir, "log")
    csv_path = os.path.join(output_dir, "result.csv")
    # ---------------------------
    print('-'*50)
    print("* {0} : {1}".format("img_dir", img_dir))
    print("* {0} : {1}".format("json_path", json_path))
    print("* {0} : {1}".format("log_path", log_path))
    print("* {0} : {1}".format("csv_path", csv_path))
    print('-'*50)
    # ---------------------------

    # json path file
    img_name_json_dict = get_json_dict(json_path)

    # model_list
    assign_model_list = args.modelList.strip().split(',')

    # get img
    img_path_list = list(FileOperationUtil.re_all_file(img_dir, lambda x:str(x).endswith(('.jpg', '.JPG', '.png'))))

    # init log
    dete_log = SaveLog(log_path, len(img_path_list), csv_path)
    dete_log.read_img_list_finshed()

    # warm up
    print("* start warm model ")
    scriptName = os.path.basename(__file__).split('.')[0]
    all_model_list = ['nc' ,'jyzZB', 'fzc', 'fzcRust', 'ljcRust', 'fncDK', 'kkxTC', 'kkxQuiting', 'kkxRust', 'waipo', 'xjQX']
    model_dict = model_restore(args, scriptName, all_model_list)
    print("* warm model success ")

    # dete
    for each_img_path in img_path_list:
        print(each_img_path)
        #
        each_img_name = os.path.split(each_img_path)[1]
        if each_img_name in img_name_json_dict:
            each_img_chinese_name = img_name_json_dict[each_img_name]
        else:
            each_img_chinese_name = " "
        #
        try:
            each_model_list = get_model_list_from_img_name(each_img_chinese_name, assign_model_list)
            each_dete_res = model_dete(each_img_path, model_dict, each_model_list)
            dete_log.add_csv_info(each_dete_res, each_img_name)
        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])
            print(e.__traceback__.tb_lineno)

        dete_log.add_log(each_img_name)
        #
        print('-'*50)

    #
    dete_log.close()

    
    
        
        
        
        
        
        
        
