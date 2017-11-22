# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 17:44:32 2017

@author: Owner
"""

# !/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

#linespace, evenly spaced from 0 to 20, in 1000 increments
#i.e. increments of 0.02
x = np.linspace(0, 20, 1000)

y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, "-g", label = "sine")
plt.plot(x, y2, "-b", label = "cosine")
plt.legend(loc = "upper right")
plt.ylim(-1.5, 1.5)
plt.show()


