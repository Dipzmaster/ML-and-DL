# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 16:24:19 2021

@author: HP
"""

one = 1.0
one_third = 1.0/3.0
zero = one - one_third - one_third - one_third
print('one =', one, ' one_third =', one_third, ' zero =', zero)

# File dividedanger.py
# Get two integers from the user
print('Please enter two numbers to divide.')
dividend = int(input('Please enter the dividend: '))
divisor = int(input('Please enter the divisor: '))
# Divide them and report the result
print(dividend, '/', divisor, "=", dividend/divisor)

# Get a number from the user
value = int(input('Please enter a number to cut in half: '))
# Report the result
print(value/2)