# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import os
from PIL import Image,ImageEnhance
import cv2
import numpy as np
from Report.FileOperationUtil import FileOperationUtil


# todo 图像的扩增代码
# todo 两种模式，一种是每一个方法在原图上做变换，一种是每一个方法也对已做变换的图片进行变换


class ImageAugmentation(object):

    def __init__(self, img_list, save_dir):
        self.save_dir = save_dir
        self.img_list = img_list
        self.mode = 0  # mode == 0 所有变换只针对原图， mode == 1 所有变换针对原图和变换过的图

    def change_img_light(self, img_path, index=None):
        """调节图片明暗度, index < 0 变暗 > 0 变亮 """
        if not index:
            index = [0.75, 1.15]

        img_obj = Image.open(img_path)
        img_name = os.path.splitext(os.path.split(img_path)[1])[0]
        img_list = []
        for each_index in index:
            each_shine = img_obj.point(lambda p: p * each_index)
            each_shine = each_shine.convert('RGB').convert('RGB')
            each_save_path = os.path.join(self.save_dir, "{0}_shine({1}).jpg".format(img_name, str(each_index)))
            each_shine.save(each_save_path, quality=95)
            img_list.append(each_save_path)
        return img_list

    def change_img_contrast(self, img_path, index=None):
        """调节图片饱和度，index，改变的程度"""
        if index is None:
            index = [0.85, 1.25]

        img_obj = Image.open(img_path)
        img_name = os.path.splitext(os.path.split(img_path)[1])[0]

        img_list = []
        for each_index in index:
            img_obj = ImageEnhance.Color(img_obj).enhance(each_index)
            img_obj = img_obj.convert('RGB')
            each_save_path = os.path.join(self.save_dir, "{0}_saturation({1}).jpg".format(img_name, str(each_index)))
            img_obj.save(each_save_path, quality=95)
            img_list.append(each_save_path)
        return img_list

    def rgb_to_gray(self, img_path):
        """转为灰度图像"""
        img_obj = Image.open(img_path).convert('L')
        img_name = os.path.splitext(os.path.split(img_path)[1])[0]
        save_path = os.path.join(self.save_dir, "{0}_gray.jpg".format(img_name))
        img_obj.save(save_path, quality=95)
        return [save_path]

    def change_img_channel_order(self, img_path, order=None):
        """通道调换，打乱图像通道之间的顺序"""
        if order is None:
            order = [[2, 0, 1], [1, 2, 0]]

        img = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)
        img_list = []
        for each_order in order:
            if list(each_order) == [0, 1, 2]:
                continue

            im = img[..., each_order]
            img_name = os.path.splitext(os.path.split(img_path)[1])[0]
            save_path = os.path.join(self.save_dir, "{0}_channel_switch({1}).jpg".format(img_name, each_order))
            cv2.imencode('.jpg', im)[1].tofile(save_path)
            img_list.append(save_path)
        return img_list

    def add_gasuss_noise(self, img_path, mean=0, var=0.04):
        """ 添加高斯噪声, mean : 均值, var : 方差"""
        img_array = np.array(Image.open(img_path))
        image = np.array(img_array / 255.0, dtype=float)  # 设置值域为 （0, 1）
        noise = np.random.normal(mean, var ** 0.5, image.shape)
        out = image + noise
        out = np.clip(out, 0, 1.0)
        out = np.uint8(out * 255)
        img_name = os.path.splitext(os.path.split(img_path)[1])[0]
        save_path = os.path.join(self.save_dir, "{0}_gasuss_noise({1}).jpg".format(img_name, (mean, var)))
        img = Image.fromarray(out)
        img.save(save_path)
        return [save_path]

    def rotation(self, img_path, rotation_list=None):
        """根据角度进行旋转，rotation_list 旋转角度列表"""
        if rotation_list is None:
            rotation_list = [90, 180, 270]

        img = Image.open(img_path)
        img_name = os.path.splitext(os.path.split(img_path)[1])[0]
        img_list = []
        for each_rotation in rotation_list:
            rotation_img = img.rotate(each_rotation) # 逆时针的旋转角度
            each_save_path = os.path.join(self.save_dir, "{0}_rotation({1}).jpg".format(img_name, each_rotation))
            rotation_img.save(each_save_path, quality=95)
            img_list.append(each_save_path)
        return img_list

    def flip(self, img_path):
        """左右翻转"""
        img_name = os.path.splitext(os.path.split(img_path)[1])[0]
        save_path = os.path.join(self.save_dir, "{0}_flip.jpg".format(img_name))
        imgObj = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), 1)
        flipImg = cv2.flip(imgObj, 1)
        cv2.imencode('.jpg', flipImg)[1].tofile(save_path)
        return [save_path]

    def deal_img(self, img_list,  func):
        """根据传入的 func 图像处理方法对 img_list 中的图像进行处理"""
        img_list_new = []
        for each_img in img_list:
            # img_list_new.extend(func(each_img, self.save_dir))
            try:
                img_list_new.extend(func(each_img))
            except:
                print(each_img)
        return img_list_new

    def do_process(self):
        """主流程"""
        if self.mode == 0:
            for img_index, each_img in enumerate(self.img_list):
                print(img_index, each_img)
                self.change_img_light(each_img)
                self.change_img_contrast(each_img)
                self.rgb_to_gray(each_img)
                self.change_img_channel_order(each_img)
                self.add_gasuss_noise(each_img)
                self.rotation(each_img)
                self.flip(each_img)
        elif self.mode == 1:
            img_list = self.img_list.copy()
            img_list = self.deal_img(img_list, self.change_img_light)
            img_list = self.deal_img(img_list, self.change_img_contrast)
            # img_list = self.deal_img(img_list, self.rgb_to_gray)
            # img_list = self.deal_img(img_list, self.change_img_channel_order)
            img_list = self.deal_img(img_list, self.add_gasuss_noise)
            # img_list = self.deal_img(img_list, self.rotation)
            # img_list = self.deal_img(img_list, self.flip)

if __name__ == "__main__":

    # img_folder = r"C:\Users\14271\Desktop\del\test_augment\in"
    # out_folder = r"C:\Users\14271\Desktop\ImageAugmentation"
    out_folder = r"C:\Users\14271\Desktop\bbb"

    # for each_dir in os.listdir(out_folder):
    #     each_dir_path = os.path.join(out_folder, each_dir)
    #     imgs_list = FileOperationUtil.re_all_file(each_dir_path, lambda x:str(x).endswith('.jpg'))  # 遍历找到文件夹中符合要求的图片
    #     a = ImageAugmentation(imgs_list, each_dir_path)
    #     a.mode = 0
    #     a.do_process()


    imgs_list = FileOperationUtil.re_all_file(out_folder, lambda x:str(x).endswith('.jpg'))  # 遍历找到文件夹中符合要求的图片
    a = ImageAugmentation(imgs_list, r"C:\Users\14271\Desktop\ccc")
    a.mode = 1
    a.do_process()

