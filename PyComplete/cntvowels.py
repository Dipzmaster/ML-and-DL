# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 20:17:19 2021

@author: HP
"""

word = input('Enter text: ')
vowel_count = 0
for c in word:
    if c == 'A' or c == 'a' or c == 'E' or c == 'e' \
        or c == 'I' or c == 'i' or c == 'O' or c == 'o':
            print(c, ', ', sep='', end='') # Print the vowel
            vowel_count += 1 # Count the vowel
print(' (', vowel_count, ' vowels)', sep='')