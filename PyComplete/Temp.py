# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 16:32:12 2021

@author: HP
"""

# Prompt user for temperature to convert and read the supplied value
degreesF = float(input('Enter the temperature in degrees F: '))
# Perform the conversion
degreesC = 5/9*(degreesF - 32)
# Report the result
print(degreesF, 'degrees F =', degreesC, 'degrees C')