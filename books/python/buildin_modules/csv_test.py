# -*- coding: utf-8  -*-
# -*- author: jokker -*-


import csv
from JoTools.utils.CsvUtil import CsvUtil
import _csv

# __all__ 的使用
# __next__ 的使用
#




csv_path = r"C:\Users\14271\Desktop\del\results.csv"


with open(csv_path, encoding='utf-8') as csvfile:
    # csv_reader = csv.reader(csvfile)
    csv_reader = csv.DictReader(csvfile)

    a = next(csv_reader)

    print(a)

    print(csv_reader.fieldnames)

    b = csv_reader[1]

    print(b)

    # for row in csv_reader:
    #     print(row)

    print(csv.__version__)



