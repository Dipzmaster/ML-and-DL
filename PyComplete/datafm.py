# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 15:24:53 2021

@author: HP
"""
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 1, 4, 3, 5, 2, 3, 4, 1],
                   'B': [12, 14, 11, 16, 18, 18, 22, 13, 21, 17],
                   'C': ['a', 'a', 'b', 'a', 'b', 'c', 'b', 'a', 'b', 'a']})

#print(df)

df.describe()