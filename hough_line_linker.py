# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 17:37:29 2017

@author: jarro
"""

# !/usr/bin/python

import numpy as np
import cv2

def hough_line_linker(lines, edge):
    l,n,m = lines.shape
    L = np.zeros((l,m+1))
    L[:, 0:4] = plines[:,0,:]
    L[:, 4] = np.arctan2((L[:,3] - L[:,1]),(L[:,2] - L[:,0]))
    
        