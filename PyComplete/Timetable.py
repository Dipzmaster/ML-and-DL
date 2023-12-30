# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 20:19:01 2021

@author: HP
"""

# Get the number of rows and columns in the table
size = int(input("Please enter the table size: "))
# Print a size x size multiplication table
for row in range(1, size + 1):
    for column in range(1, size + 1):
        product = row*column # Compute product
        print('{0:4}'.format(product), end='') # Display product
    print()