# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 14:49:44 2021

@author: HP
"""

def increment(x):
    print("Beginning execution of increment, x =", x)
    x += 1 # Increment x
    print("Ending execution of increment, x =", x)
def main():
    x = 5
    print("Before increment, x =", x)
    increment(x)
    print("After increment, x =", x)
main()