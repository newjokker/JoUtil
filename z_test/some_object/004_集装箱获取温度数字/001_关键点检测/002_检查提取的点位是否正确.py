# -*- coding: utf-8  -*-
# -*- author: jokker -*-



import pandas as pd


data = pd.read_csv(r'C:\Users\14271\Desktop\save_dir\points.csv')

ix = 0

a = data.iloc[ix,1:].tolist()

print(a)

# print(data)





