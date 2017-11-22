# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 12:26:03 2017
A group of functions for RANSAC line fitting.  Potentially applicable to both
2D and 3D, although at current only testing for 2D.
@author: jarron
"""

# !/usr/bin/python
import numpy as np
import cv2

#RANSAC_line_fitting
#uses RANSAC to find multiple lines in a dataset
#INPUT-------------------------------------------------------------------------
#points:    n x 2 np.array that represent the coordinates of the points
#racc:      acccuray of the radius (threshold of the distance from the point\
#           to the line for it to be an inlier
#aacc:      accuracy for the angle of the line generated (angular fit)
#its:       maximum number of iterations performed
#mlines:    boolean representing whether to iteratively find multiple lines in
#           data(true) or not (false). If false only one line is fit to the data
#OUTPUT------------------------------------------------------------------------
def RANSAC_line_fitting(points, racc, aacc, its, mlines):
    if mlines == True:
        
        
        