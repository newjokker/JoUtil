# -*- coding: utf-8  -*-
# -*- author: jokker -*-


class Model(object):

    def __init__(self):
        # self.model = None
        pass

    def model_restore(self, args):
        # import
        # model_restore
        pass

    def model_detect(self, img_path=None, img_ndarry=None):
        pass



# todo args 去除这个参数，使用其他的形式进行代替

import os, sys
this_dir = os.path.dirname(__file__)
lib_path = os.path.join(this_dir, '..')
sys.path.insert(0, lib_path)
#
from lib.detect_libs.fasterDetectionPyTorch import FasterDetectionPytorch
from lib.detect_libs.vggClassify import VggClassify
from lib.detect_libs.clsViTDetection import ClsViTDetection


class FzcBrokenRust(Model):

    def __init__(self):
        super().__init__()
        self.model_fzc_step_1 = None
        self.model_fzc_step_2 = None
        self.model_fzc_rust = None
        #
        self.activate_model_dict = {"fzc_broken":False, "fzc_rust":False}

    def model_restore(self, args):
        """模型预加载"""
        # todo 模型的加载是可以并行加载的，在所有模型一起加载的时候改一下
        self.model_fzc_step_1 = FasterDetectionPytorch(args, "fzc_step_one", scriptName)
        self.model_fzc_step_1.model_restore()
        #
        self.model_fzc_step_2 = VggClassify(args, "fzc_step_new", scriptName)
        self.model_fzc_step_2.model_restore()
        #
        self.model_fzc_rust = ClsDetectionPyTorch(args, "fzc_rust", scriptName)
        self.model_fzc_rust.model_restore()

    def model_detect(self, img_path=None, img_ndarry=None):
        """模型检测"""

        # fixme 这边最好能直接使用 ndarry 作为传入的参数，而不是一遍遍地去解析 jpg 文件，获取 ndarry

        try:
            # ----------------------------------------------------------------------------------------------------------
            # step_1
            dete_res_fzc = self.model_fzc_step_1.detectSOUT(path=img_path, image_name=name)
            # ----------------------------------------------------------------------------------------------------------
            # step_2
            for each_dete_obj in dete_res_fzc:
                crop_array = dete_res_fzc.get_sub_img_by_dete_obj(each_dete_obj, RGB=False, augment_parameter=[0.1, 0.1, 0.1, 0.1])
                new_label, conf = self.model_fzc_step_2.detect_new(crop_array, name)
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
                # ----------------------------------------------------------------------------------------------------------
                # step 3 fzc rust
                if self.activate_model_dict['fzc_broken']:
                    # rust
                    if new_label in ["yt", "zd_yt"]:
                        crop_array_rust = dete_res_fzc.get_sub_img_by_dete_obj(each_dete_obj, RGB=False)
                        rust_index, rust_f = model_fzc_rust.detect(crop_array_rust)
                        rust_label = ["fzc_normal", "fzc_rust"][int(rust_index)]
                        rust_f = float(rust_f)
                        #
                        each_dete_rust = each_dete_obj.deep_copy()
                        each_dete_rust.tag = rust_label
                        # each_dete_rust.conf = rust_f
                        #
                        dete_res_all.add_obj_2(each_dete_rust)

        except Exception as e:
            print(e)
            print(e.__traceback__.tb_frame.f_globals["__file__"])
            print(e.__traceback__.tb_lineno)































