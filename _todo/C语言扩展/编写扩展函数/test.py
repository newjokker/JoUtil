import os
import sys
import time

this_path = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, this_path)
from lib import jo_test as ld

xml_file_path = os.path.join(this_path, "xml")

from JoTools.utils.DecoratorUtil import DecoratorUtil


@DecoratorUtil.time_this
def xml_read_in_python():
    dict_list = []
    for xml_name in os.listdir(xml_file_path):
        xml_path = os.path.join(xml_file_path, xml_name)
        #print(xml_name)
        dict_list.append(jd.parse_xml_as_txt(xml_path))
@DecoratorUtil.time_this
def xml_read_in_c():
    dict_list = []
    for xml_name in os.listdir(xml_file_path):
        xml_path = os.path.join(xml_file_path, xml_name)
        #print(xml_name)
        a = ld.parse_xml_as_txt(xml_path)
    print(a)

def test3():
    a = jd.parse_xml_as_txt("./xml/ee9fe6e12ba8603846dc2ab7ba424f23.xml")
    b = ld.parse_xml_as_txt("./xml/ee9fe6e12ba8603846dc2ab7ba424f23.xml")
    #print(a)
    print(sys.getrefcount(a['path']))
    print()
    #print(b)
    print(sys.getrefcount(b['path']))

if __name__ == "__main__":

    print(ld.test_001(12, '1213', 13))

            
