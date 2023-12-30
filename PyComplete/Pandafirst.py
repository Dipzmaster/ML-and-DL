# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 15:18:40 2021

@author: HP
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

values = np.random.randn(100)
s = pd.Series(values)
s.plot(kind='hist', title='NDRV')
plt.show()