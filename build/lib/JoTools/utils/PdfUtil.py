# -*- coding: utf-8  -*-
# -*- author: jokker -*-

"""读写 PDF 文件信息"""

# import PDFMiner
import pdfkit
from Report.FileOperationUtil import FileOperationUtil
from Report.StrUtil import StrUtil


# 读取 pdf 中的内容:http://www.ityouknow.com/python/2020/01/02/python-pdf-107.html

# url页面转化为pdf
# url = r'https://blog.csdn.net/qq_41185868/article/details/79907936#pdfkit%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95'
file_path = r'C:\Users\Administrator\Desktop\SnowDepth.pdf'
dir_path = r"C:\data\深度学习资料\001_要打印的论文\detection"
# pdfkit.from_url(url, file_path)

# 文本内容转化为pdf
# pdfkit.from_string(u"jokker，呵呵，你说呢", file_path)

pdf_path_list = FileOperationUtil.re_all_file(dir_path, lambda x:str(x).endswith('.pdf'))

for each_pdf_path in pdf_path_list:
    # print(each_pdf_path)
    pass


print(pdf_path_list[1])






# # 文件转化为pdf
# pdfkit.from_file(file, file_path)
#
# # 也可以是打开的文件
# with open('file.html') as f:
#     pdfkit.from_file(f, 'out.pdf')
#
# print('OK')


# fixme 读取 pdf 中的文字

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextBoxHorizontal
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

path = r"C:\Users\14271\Desktop\算法模型开发管理程序文件_V1.1_Draft.pdf"
# path = each_pdf_path

# 用文件对象来创建一个pdf文档分析器
praser = PDFParser(open(path, 'rb'))
# 创建一个PDF文档
doc = PDFDocument()
# 连接分析器 与文档对象
praser.set_document(doc)
doc.set_parser(praser)

# 提供初始化密码
# 如果没有密码 就创建一个空的字符串
doc.initialize()

# 检测文档是否提供txt转换，不提供就忽略
if not doc.is_extractable:
    raise PDFTextExtractionNotAllowed
else:
    # 创建PDf 资源管理器 来管理共享资源
    rsrcmgr = PDFResourceManager()
    # 创建一个PDF设备对象
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    # 创建一个PDF解释器对象
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # 循环遍历列表，每次处理一个page的内容
    res = []
    for page in doc.get_pages():
        interpreter.process_page(page)
        # 接受该页面的LTPage对象
        layout = device.get_result()
        # 这里layout是一个LTPage对象，里面存放着这个 page 解析出的各种对象
        # 包括 LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等
        for x in layout:
            if isinstance(x, LTTextBox):
                res.append(x.get_text().strip())
                print(x.get_text().strip())
                if "yolo" in x.get_text():
                    # print(x.get_text().strip())
                    pass
                # x = StrUtil.remove_assign_character(x.get_text(), "\n")
                # print(x)
            elif isinstance(x, LTTextBoxHorizontal):
                print(x)


print("OK")














