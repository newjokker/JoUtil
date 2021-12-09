# -*- coding: utf-8  -*-
# -*- author: jokker -*-

import time
from JoTools.utils.JsonUtil import JsonUtil
from JoTools.txkj.eagleUtil import EagleMetaData, EagleUtil, EagleMTimes, EagleTags

# 将新数据的 json.info 直接放到 edgal 数据库下面，看看能不能自动化读取

# 增加标签需要修改三个地方（1）metadata.json （2）mtime.json (3) tags.json

    # 在元数据中增加 tags 信息
    # 更新元数据中的 lastModified 字段信息
    # 更新 mtime.json 中的信息，与元数据中保持一致
    # tags.json 中添加新标签的信息

# 每次更新新标签之后将 lastModified 字段和 mtime 中字典的字段对应修改即可，修改的时间直接是 time.time()


tag_json_path = r"C:\data\edgle\FZCTEST.library\tags.json"
mtime_json_path = r"C:\data\edgle\FZCTEST.library\mtime.json"
meta_json_path = r"C:\data\edgle\FZCTEST.library\images\KDH5EVWARA22B.info\metadata.json"

tags = EagleTags()
tags.load_from_json(tag_json_path)

mtime = EagleMTimes()
mtime.load_from_json(mtime_json_path)

meta_data = EagleMetaData()
meta_data.load_atts_from_json(meta_json_path)

print(meta_data.name)


# 增加 tags
new_tag = "test_chis"
meta_data.add_tag(new_tag)
assign_id = meta_data.id
new_time = int(time.time() * 1000)
meta_data.modification_time = new_time
mtime.update_assign_id(assign_id, new_time)
tags.add_tags(new_tag)

meta_data.save_to_json_file(meta_json_path)
mtime.save_to_json_file(mtime_json_path)
tags.save_to_json_file(tag_json_path)

# ----------------------------

"""

* 存在未考虑的区域

* 九类比较的时候，我们除了小金具很多模型未开发

* 他们标图的标准是以人眼能识别就可以标，所以我们后面考虑小图过滤操作是否需要，我们的标准测试集也需要和客户一样的标注方法

* 定位数据对模型时间效率要求比较高，一共 50G 数据，定位数据告诉数据拍的是那些部位，可以根据部位选择对应的几个模型进行

* 运行的环境 GPU 是 11 G，

* 因为 运行环境限制 需要将大的模型拆成几个小的部分，分别运行

* 是否可以训练一个模型区分九大类，一个简单的分类模型先将 9 类进行划分，再在基础上进行模型检测，9 类分类模型并不是放在
某一个模型的前面，而是单独的一个模型，与其他模型并行跑

* 我们现在的数据还是不全，开口销和防振锤都出现了之前没有训练过的模式

* 需要将模型代码标准化 （1）鸟巢模型 debug 模式没输出画图结果 （2）fzc rust 没输出 xml，使用的画图代码等不统一，临时修改
难度较大，算法内部可以集体维护一个工具包，统一基础功能的实现方式

* 比赛用到的模型的开发侧重点放在出现较为频繁的地方，不用在比较难但是不常出现或人眼难以判别的地方花太多的精力（开口销的亮洞）

* 我们目前缺陷分类和电科院的缺陷分类有挺大的区别，需要从客户的角度考虑，尝试调整

"""

