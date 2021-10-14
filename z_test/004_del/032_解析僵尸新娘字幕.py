# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.utils.TxtUtil import TxtUtil

file_path = r"C:\Users\14271\Desktop\del\Mary.And.Max.srt.srt"


digit_line = False
chinese_line = False

english_lines = []

with open(file_path, 'r', encoding='GBK') as txt_file:
    english_line = True
    while True:
        each = next(txt_file)
        if each.strip().isdigit():
            digit_line = each
            time_line = next(txt_file)
            chinexe_line = next(txt_file)
            english_line = next(txt_file).strip()

            # print(digit_line)
            # print(time_line)
            # print(chinese_line)
            print(english_line)

            if english_line == 'end':
                break
            else:
                english_lines.append([english_line + '\n' + '\n'])
        else:
            print(each)

TxtUtil.write_table_to_txt(english_lines, r"C:\Users\14271\Desktop\del\Mary.And.Max.txt")

