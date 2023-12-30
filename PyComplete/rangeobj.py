# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 20:14:25 2021

@author: HP
"""

for i in range(10):
    print(i, end=' ') # Print i as served by the range object
    if i == 5:
        i = 20 # Change i inside the loop?
    print('({})'.format(i), end=' ')
print()