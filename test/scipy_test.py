#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2019/6/14 17:25
@Author  : xumj
'''

import numpy as np
from scipy import linalg as LA
c = np.mat([[3, 2, 0], [1, 1, 0], [0, 5, 1]])
d = np.matrix([0, -1, 2])
inv = LA.inv(c)
