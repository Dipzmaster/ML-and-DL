# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 15:33:00 2021

@author: HP
"""

import pandas as pd
import numpy as np
num_securities = 1000
num_periods = 1000
period_frequency = 'W'

start_date = '2000-12-31'
np.random.seed([3,1415])
means = [0, 0]
covariance = [[ 1., 5e-3],
[5e-3, 1.]]
# generates to sets of data m[0] and m[1] with ~0.005 correlation
m = np.random.multivariate_normal(means, covariance,
(num_periods, num_securities)).T

ids = pd.Index(['s{:05d}'.format(s) for s in range(num_securities)], 'ID')
tidx = pd.date_range(start=start_date, periods=num_periods, freq=period_frequency)