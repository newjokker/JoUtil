

from JoTools.txkjRes.deteRes import DeteRes
from JoTools.utils.FileOperationUtil import FileOperationUtil
from JoTools.utils.RandomUtil import RandomUtil
from JoTools.operateDeteRes import OperateDeteRes



xml_dir = r"E:\算法培育-6月样本"

for each in FileOperationUtil.re_all_file(xml_dir, lambda x:str(x).endswith('.xml')):
    print(each)
    a = DeteRes()
    a.xml_path = each
    a.save_to_xml(each)


