# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from types import MethodType




def fake_deteSOUT(self, path=None, image=None, image_name="default.jpg", output_type='txkj'):
    """mock deteSOUT"""
    # fixme 检测结果使用 xml 进行保存，分类结果使用 txt 来保存
    # fixme 同一个 md5 对于不同的模型出来的结果是不一样的，处理 md5 之外还要标记模型名字


    if isinstance(path, str) and image is None:
        image = cv2.imdecode(np.fromfile(image, dtype=np.uint8), 1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image = np.ascontiguousarray(image)
    md5 = HashLibUtil.get_str_md5(image)
    xml_path = os.path.join(self.mock_dir, f"{self.objName}_{md5}.xml")
    txt_path = os.path.join(self.mock_dir, f"{self.objName}_{md5}.txt")

    if os.path.exists(xml_path):
        return DeteRes(xml_path=xml_path)
    elif os.path.exists(txt_path):
        with open(txt_path) as txt_file:
            class_index = txt_file.readline().strip()
            return int(class_index)
    else:
        file_path = os.path.join(self.mock_dir, f"{self.objName}_{md5}.txt")
        raise ValueError(f"* no txt founded : {file_path}")


# 修改类属性
# YOLOV5Detection.detectSOUT = fake_deteSOUT
# 修改实例属性
kkx_prebase.detectSOUT = MethodType(fake_deteSOUT, kkx_prebase)
model_xjQX_kkx.detectSOUT = MethodType(fake_deteSOUT, model_xjQX_kkx)

