# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 16:44:03 2021

@author: HP
"""

print('Please enter two numbers to divide.')
dividend = int(input('Please enter the first number to divide: '))
divisor = int(input('Please enter the second number to divide: '))
# If possible, divide them and report the result
if divisor != 0:
    print(dividend, '/', divisor, "=", dividend/divisor)