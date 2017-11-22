# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 17:51:42 2017

@author: Owner
"""

# !/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

XY = np.array([[2,2],[2,5],[5,1],[5,3],[5,5],[8,5],[8,8]], np.float)

theta = np.linspace(0,np.pi,180,dtype = 'float')
r = [[0 for m in range(181)]for n in range(len(XY))]
i = 0
for n in XY:
    r[i] = n[0]*np.cos(theta) + n[1]*np.sin(theta)
    i+=1

color = ["b","g","r","c","m","y","k","w"]
j = 0
for m in r:
    plt.plot(theta, m, color[j],label = str(j+1))
    plt.legend(loc = "upper right")
    j += 1
plt.xlabel("theta (in radians)")
plt.ylabel("radius")
plt.title("Hough Space Visualization")
plt.show()

j = 0;
for n in XY:
    plt.scatter(n[0], n[1], c = color[j])
    j+=1
plt.plot([2,5,8],[2,5,8], "-r")
plt.plot([2,5,8],[5,5,5],"-b")
plt.plot([5,5,5],[1,3,5],"-g")
plt.show()

