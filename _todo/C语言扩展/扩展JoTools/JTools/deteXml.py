# -*- coding: utf-8  -*-
# -*- author: jokker -*-

def parse_xml_as_txt(xml_path):
    """使用读取存文本的方式读取 xml """

    def parse_assign_line(each_xml_line, assign_tag):
        """解析指定行中的指定标签"""
        return each_xml_line.strip()[len(assign_tag) + 2: -len(assign_tag) - 3]

    xml_info = {'size': {'height': -1, 'width': -1, 'depth': -1},
                'filename': '', 'path': '', 'object': [], 'folder': '',
                'segmented': '', 'source': ''}

    with open(xml_path, 'r', encoding='utf-8') as xml_file:
        each_line = next(xml_file)
        while each_line:
            each_line = each_line.strip()

            if each_line.startswith('<filename>'):
                xml_info['filename'] = parse_assign_line(each_line, 'filename')
            elif each_line.startswith('<folder>'):
                xml_info['folder'] = parse_assign_line(each_line, 'folder')
            elif each_line.startswith('<height>'):
                xml_info['size']['height'] = float(parse_assign_line(each_line, 'height'))
            elif each_line.startswith('<width>'):
                xml_info['size']['width'] = float(parse_assign_line(each_line, 'width'))
            elif each_line.startswith('<depth>'):
                xml_info['size']['depth'] = float(parse_assign_line(each_line, 'depth'))
            elif each_line.startswith('<path>'):
                xml_info['path'] = parse_assign_line(each_line, 'path')
            elif each_line.startswith('<segmented>'):
                xml_info['segmented'] = parse_assign_line(each_line, 'segmented')
            elif each_line.startswith('<source>'):
                xml_info['source'] = parse_assign_line(each_line, 'source')
            elif each_line.startswith('<object>'):
                each_obj = {'name': '', 'prob': -1, 'id':-1, 'des':'','crop_path':'',
                            'bndbox': {'xmin': -1, 'xmax': -1, 'ymin': -1, 'ymax': -1}}
                while True:
                    each_line = next(xml_file)
                    each_line = each_line.strip()

                    if each_line.startswith('</object>'):
                        xml_info['object'].append(each_obj)
                        break
                    elif each_line.startswith('<name>'):
                        each_obj['name'] = parse_assign_line(each_line, 'name')
                    elif each_line.startswith('<prob>'):
                        each_obj['prob'] = float(parse_assign_line(each_line, 'prob'))
                    elif each_line.startswith('<id>'):
                        each_obj['id'] = float(parse_assign_line(each_line, 'id'))
                    elif each_line.startswith('<des>'):
                        each_obj['des'] = parse_assign_line(each_line, 'des')
                    elif each_line.startswith('<crop_path>'):
                        each_obj['crop_path'] = parse_assign_line(each_line, 'crop_path')
                    elif each_line.startswith('<xmin>'):
                        each_obj['bndbox']['xmin'] = float(parse_assign_line(each_line, 'xmin'))
                    elif each_line.startswith('<xmax>'):
                        each_obj['bndbox']['xmax'] = float(parse_assign_line(each_line, 'xmax'))
                    elif each_line.startswith('<ymin>'):
                        each_obj['bndbox']['ymin'] = float(parse_assign_line(each_line, 'ymin'))
                    elif each_line.startswith('<ymax>'):
                        each_obj['bndbox']['ymax'] = float(parse_assign_line(each_line, 'ymax'))

            elif each_line.startswith('</annotation>'):
                return xml_info

            each_line = next(xml_file)

