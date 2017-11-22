# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:47:51 2017

@author: Owner
"""

#! /usr/bin/python

import numpy as np

x = [5,10,15,20,25]
#declare as an empty list
y = []
for count in x:
    y.append(count/5)

print("Old School :\nx = {}\ny ={} \n".format(x,y))

z = [n/5 for n in x]
print("Too cool 4 school:\n z={}".format(z))

a = np.array([5, 10, 15, 20, 25])
b = np.true_divide(a,5)
np.set_printoptions(precision = 3)
print("\na = ",a,"\nb = ",b)

