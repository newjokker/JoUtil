# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkj.ucDatasetUtil import UCDatasetUtil



# CPP 代码的编写

# 将手头的数据生成 ucDataset.json 用于复用

# 想谁便看看就先下载 指定的个数来看

# todo 将转换这块工作也交给服务端去做，这样就不需要在本地下载转化的代码了

# todo 使用的场景，测试代码在不同的服务器上进行倒腾

# todo 测试代码标准化，完善一个测试数据集合，专门用于测试，先不要求测试图片和训练图片分开

# todo 手头数据生成 非官方的 数据集


save_dir = r"C:\Users\14271\Desktop\del\save_img"

a = UCDatasetUtil(r"C:\Users\14271\Desktop\del\test.json", "192.168.3.111", 11101)

a.save_img_xml_json(save_dir=save_dir, need_img=True, need_json=False, need_xml=True)