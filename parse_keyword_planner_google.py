#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd

# read columns
with open('key.csv','r',encoding='utf-16') as fi:
    names = None
    for line in fi.readlines():
        names = line.split('\t')
        break

names = [i.strip() for i in names]
print(names)


df = pd.read_csv('key.csv',skiprows=1,nrows=None,
                 encoding='utf-16',delimiter='\t',header=None,names=names)

print(df.shape)
print(df.head(2).append(df.tail(2)))

# Read another file
url = "https://raw.githubusercontent.com/sumandevkota/SHARED/main/Tshirt.csv"

df = pd.read_csv(url,skiprows=1,nrows=None,
                encoding='utf-16',delimiter='\t',header=None,
                names=names)

print(df.shape)
print(df.head(2).append(df.tail(2)))