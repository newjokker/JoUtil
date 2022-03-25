# -*- coding: utf-8  -*-
# -*- author: jokker -*-
from itertools import groupby

a = ['123,.', '45645.jkj', '4555555555555645646.....jiji']

for av in a:
    avb = [key for key,groupv in groupby(av)]
    print("".join(avb))

#print( ".".join(list(map(lambda x:x.split("."), a))))

# def point_to_one(assign_str):
#
#     res = ""
#
#     for i in assign_str:
#         if i == '.' and len(res) >0 :
#             if res[0]=='.':
#                 pass
#             else:
#                 pass









# print('.'.join(list(map(lambda x:x.split("."), a))))


#
# print(".".join(list(map(lambda x:x.replace('.', ''), a))))


# '123'.replace('.', '')