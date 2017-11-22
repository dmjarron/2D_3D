# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 18:05:04 2017

@author: David Jarron
"""

# !/usr/bin/python

import cv2
import numpy as np
import matplotlib.pyplot as plt
#import hough_line_linker as hll

img = cv2.imread('IMG_3380.JPG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height, width = gray.shape
# can aslo unse IMREAD_COLOR or IMREAD_UNCHANGED

#imshow using cv2 basic
#cv2.imshow('image',img)
#cv2.waitKey()

#plot using matplot lib
#plt.imshow(img, cmap='gray', interpolation = 'bicubic')
#plt.plot([500,1000],[800,1000],'c', linewidth = 3)
#plt.show()

#save image to file using cv2 
#cv2.imwrite('testim.png',img)

# canny edge detection of image

edges = cv2.Canny(gray, 400, 50)
#edges = cv2.Canny(gray, 500, 50)

#kern = np.ones((2,2),np.uint8)
#
#edges = cv2.morphologyEx(edges, cv2.MORPH_OPEN,kern)

h2 = int(height / 2)
w2 = int(width / 2)

cv2.namedWindow("edges", cv2.WINDOW_NORMAL)
imS = cv2.resize(edges, (width, height))
cv2.imshow("edges", imS)
cv2.waitKey(10)
cv2.destroyAllWindows()
cv2.imwrite('edges.jpg', edges)


# Hough transform to detect lines in image from edges
lines = cv2.HoughLines(edges,1,np.pi/180,200)
for line in lines:
    rho = line[0][0]
    theta = line[0][1]      
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imwrite('houghlines3.jpg',img)

# Probabilistic Hough Transform
plines = cv2.HoughLinesP(edges,0.5,np.pi/360,30,100,5)
img1 = cv2.imread('edges.jpg')
for pline in plines:
    x1 = pline[0][0]
    y1 = pline[0][1]
    x2 = pline[0][2]
    y2 = pline[0][3]
    cv2.line(img1,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imwrite('phough_1.jpg',img1)



#two conditions work well
#first use a noisy edge image and adjust the hough parameters to be robust to that noise
# using params (edges, 0.5, pi/360, 30,100,25-50)
#OR
#Use a cleaner edge image and then a smaller maximum line dist can be chosen
#this seems to allow the majority of the edges in the edge image to be detected detected by the houghT
#(edges,0.5,np.pi/360,30,100,5) are the utilized params

# RANSAC Line Fitting
ex, ey = edges.shape
dim = ex*ey
edge_list  = np.reshape(edges,[dim,1])
#yi = i/x (integer division)
#xi = i - yi*x
yi = np.arange(dim) // ex
xi = np.arange(dim) - yi*ex

edge_w_coords = np.zeros([dim,3])
edge_w_coords[:,0] = edge_list.transpose()
edge_w_coords[:,1] = yi
edge_w_coords[:,2] = xi

edges_only = edge_w_coords[~(edge_w_coords[:,0] == 0)]
edge_coords_fin = edges_only[:,1:2]

[vx,vy,x,y] = cv2.fitLine(edges_only, cv2.DIST_L1, 0, 0.01,0.01)
cv2.line(img1,(vx,vy),(x,y),(0,255,0),2)
cv2.imwrite('ransactest_1.jpg',img1)

