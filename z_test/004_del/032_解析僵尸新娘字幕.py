# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from JoTools.utils.TxtUtil import TxtUtil

file_path = r"C:\Users\14271\Desktop\del\jsxn.srt"


digit_line = False
chinese_line = False

english_lines = []

with open(file_path, 'r', encoding='utf-8') as txt_file:
    english_line = True
    while english_line:
        each = next(txt_file)
        if each.strip().isdigit():
            digit_line = each
            time_line = next(txt_file)
            chinexe_line = next(txt_file)
            english_line = next(txt_file).strip()

            if english_line == 'end':
                break
            else:
                english_lines.append([english_line + '\n' + '\n'])

TxtUtil.write_table_to_txt(english_lines, r"C:\Users\14271\Desktop\del\jsxn.txt")

