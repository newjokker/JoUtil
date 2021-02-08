# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.utils.XmlUtil import XmlUtil


class ParseXml(object):
    """解析 xml 中的信息，将信息导出为 xml"""

    def __init__(self):
        self.__attrs = {"folder", "filename", "path", "size", "tag"}  # 所有的属性
        self.__xml_info_dict = {}  # xml 信息字典
        self.__objects_info = []
        self.__size_info = {}
        self.__source_info = {}

    def _parse_node(self, assign_node):
        """解析在字典中的关键字"""
        node_name = assign_node.nodeName
        element_info = XmlUtil.get_info_from_node(assign_node)
        self.__xml_info_dict[node_name] = element_info['value']

    def _parse_size(self, assign_node):
        """解析 size 信息"""
        for each_node in assign_node.childNodes:
            node_name = each_node.nodeName
            if node_name in ["width", "height", "depth"]:
                self.__size_info[node_name] = XmlUtil.get_info_from_node(each_node)['value']

    def _parse_xml(self, xml_path):
        """解析 xml"""
        root_node = XmlUtil.get_root_node(xml_path)  # 得到根节点
        # 遍历根节点下面的子节点
        for each_node in root_node.childNodes:
            node_name = each_node.nodeName
            if node_name in ["folder", "filename", "path", "tag", "id"]:
                self._parse_node(each_node)
            elif node_name == "size":
                self._parse_size(each_node)

    def set_attr_info(self, attr, info):
        """设置属性值"""
        if attr not in self.__attrs:
            raise ValueError("""attr should in folder, filename, path, segmented, size, source, object""")
        self.__xml_info_dict[attr] = info

    def update_xml_info(self, up_info):
        """更新 xml 字典信息，up_info: dict"""
        for each_attr in up_info:
            if each_attr not in self.__attrs:
                raise ValueError("""attr should in folder, filename, path, segmented, size, source, object""")
            else:
                self.__xml_info_dict[each_attr] = up_info[each_attr]

    def get_xml_info(self, xml_path):
        # 解析 xml
        self.__xml_info_dict = {"folder": None, "filename": None, "path": None, "tag":None}
        self._parse_xml(xml_path)
        # # 将 xml 中的信息整理输出
        self.__xml_info_dict['size'] = self.__size_info
        return self.__xml_info_dict

    def save_to_xml(self, save_path, assign_xml_info=None):
        """将 xml_info 保存为 xml 形式"""
        if assign_xml_info is None:
            assign_xml_info = self.__xml_info_dict.copy()
        # 没有值
        if not assign_xml_info:
            raise ValueError("xml info is empty")
        # 写 xml
        root = XmlUtil.get_document()
        xml_calss_1 = XmlUtil.add_sub_node(root, root, 'annotation', '')
        # 增加 "folder", "filename", "path", "segmented"
        for attr_name in ["folder", "filename", "path", "tag", "id"]:
            XmlUtil.add_sub_node(root, xml_calss_1, attr_name, assign_xml_info[attr_name])
        # 增加 size
        size_node = XmlUtil.add_sub_node(root, xml_calss_1, "size", '')
        for each_node in assign_xml_info["size"]:
            XmlUtil.add_sub_node(root, size_node, each_node, assign_xml_info["size"][each_node])
        # 保存 xml 到文件
        XmlUtil.save_xml(root, save_path)

def parse_xml(xml_path):
    """简易的函数使用版本"""
    a = ParseXml()
    xml_info = a.get_xml_info(xml_path)
    return xml_info

def save_to_xml(xml_info, xml_path):
    """保存为 xml"""
    a = ParseXml()
    a.save_to_xml(save_path=xml_path, assign_xml_info=xml_info)
