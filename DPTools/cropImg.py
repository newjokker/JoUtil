# 导入相关的库
from PIL import Image
import os
import xml.etree.ElementTree as ET
import shutil
import time
import argparse
import sys

# 这部分的内容在 databaseUtil 更为简单的实现，这部分可以删掉了


"""
* 根据 xml 中标记的物体的位置，进行截图并保存到对应的文件夹
"""


inpath = r"C:\Users\14271\Desktop\del\nc_new_img"               # 图片和xml都放在一个 xml 中
outpath = r"C:\Users\14271\Desktop\del\nc_new_img\out"          # 输出的文件夹
labels = ['L88','tk', 'LX', 'LSJ', 'td', 'fn', 'jyz', 'yx', 'nc','cc','kkx2', 'tower', 'car']  # 需要拿到的标签


class CropImg(object):

    def __init__(self):
        self.inpath = r""
        self.outpath = r""
        self.labels = []

    @staticmethod
    def args_parse():
        """解析参数"""
        ap = argparse.ArgumentParser()
        ap.add_argument("-in", "--inpath", type=str, help="input dir for .xml and .jpg")
        ap.add_argument("-out", "--outpath", type=str, help="output dir for result")
        ap.add_argument("-l", "--labels", help="labels to crop")
        input_args = ap.parse_args()
        return input_args

    @staticmethod
    def read_xml(file, img_label):
        """解析标图的 xml 信息"""
        tree = ET.parse(file)
        root = tree.getroot()
        info = dict()
        xmin, xmax, ymin, ymax = 0, 0, 0, 0
        info['width'], info['height'], info['ob'] = 0, 0, []
        for element in root.findall('size'):
            for element1 in element.findall('width'):
                info['width'] = int(element1.text)
            for element2 in element.findall('height'):
                info['height'] = int(element2.text)
        for element in root.findall('object'):
            for name in element.findall('name'):
                if name.text != img_label:
                    continue
                for element1 in element.findall('bndbox'):
                    for element2 in element1.findall('xmin'):
                        xmin = int(element2.text)
                    for element2 in element1.findall('xmax'):
                        xmax = int(element2.text)
                    for element2 in element1.findall('ymin'):
                        ymin = int(element2.text)
                    for element2 in element1.findall('ymax'):
                        ymax = int(element2.text)
                    info['ob'].append([xmin,xmax,ymin,ymax])
        return info

    @staticmethod
    def crop_pic(xml_path, img_labels):
        """获取小图"""

        # 根据 xml 路径找到 jpg 路径
        jpg_path = xml_path.replace('.xml', '.jpg')

        # 判断文件是否存在，不存在的话寻找后缀为 JPG 的是否存在，存在就将 jpg 改为 JPG
        if not os.path.exists(jpg_path):
            if os.path.exists(jpg_path[:-4] + ".JPG"):
                jpg_path = xml_path.replace('.xml', '.JPG')
            else:
                print(" xml 对应的图片数据不存在 ：{0}".format(xml_path))
                return

        file_name = jpg_path.split('\\')[-1]
        img = Image.open(jpg_path)

        for each_label in img_labels:
            xml_info = CropImg.read_xml(xml_path, each_label)  # get xml info
            count = 0
            try:
                for ob in xml_info['ob']:
                    # find crop region
                    x, y = ob[0], ob[2]
                    w, h = ob[1] - ob[0], ob[3] - ob[2]
                    # to crop
                    region = img.crop((x, y, x + w, y + h))
                    # save img
                    new_img_name = file_name[:-4] + "{0}_crop_test_{1}.jpg".format(each_label, str(count))
                    out_dir = os.path.join(outpath, each_label)
                    # create dirctory
                    if not os.path.exists(out_dir):
                       os.mkdir(out_dir)
                    # save img
                    pic_path = os.path.join(out_dir, new_img_name)
                    region.save(pic_path)
                    count = count + 1
            except Exception as e:
                print(e)

    @staticmethod
    def main(rootdir, img_labels):
        """拿到所有图片并处理"""
        img_list = os.listdir(rootdir)
        for img_index, each_img in enumerate(img_list):
           img_path = os.path.join(rootdir, each_img)
           if os.path.isfile(img_path) and each_img.endswith(".xml"):
                print(img_index, img_path)
                CropImg.crop_pic(img_path, img_labels)
           # 递归处理文件夹中的文件夹
           elif os.path.isdir(img_path):
               CropImg.main(img_path, img_labels)


if __name__=="__main__":

    # Support fixed and input parameters
    if len(sys.argv) > 1:
        args = CropImg.args_parse()
        inpath = args.inpath
        outpath = args.outpath
        labels = args.labels.strip().split(',')
    else:
        inpath = r"C:\Users\14271\Desktop\face_detection\团建图片"
        outpath = r"C:\Users\14271\Desktop\face_detection\人脸"
        labels = ['zhx', 'mhx', 'lh', 'qfm', 'csh', 'wym', 'lxz', 'jtm', 'cy', 'hyy', 'wfb', 'lj', 'ldq', 'wc', 'zyc', 'fbc', 'hcb', 'zjc', 'qk', 'wcl', 'jsq']

    startime = time.time()
    CropImg.main(inpath, labels)
    endtime = time.time()
    print("run time : {0}".format(endtime - startime))

