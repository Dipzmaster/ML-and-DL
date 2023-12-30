# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 10:52:50 2021

@author: HP
"""

from time import perf_counter
print("Enter your name: ", end="")
start_time = perf_counter()
name = input()
elapsed = perf_counter() - start_time
print(name, "it took you", elapsed, "seconds to respond")