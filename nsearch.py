# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:54:25 2017
series of functions for searching and determination
of a points neighbourhood
@author: David Jarron 10/10/2017
[1]https://stackoverflow.com/questions/4588628/find-indices-of-elements-equal
-to-zero-from-numpy-array

"""
# !/usr/bin/python

import numpy as np

"""
distancematrix generates an NxN matrix where N = length of points
which shows the distances between all points in the list.  Designed to
be superior in speed to a for loop search, although uses a lot of memory
Input: points => array of cartesian poins
"""
def distancematrix(points):
    return np.linalg.norm(points[..., np.newaxis] - points.T, 2, axis=1)

#find nearest euclidean neighburs from a point list
def neighbor(point, data, r):
    #nxn matrix with all possible distances from all
    #points in data
    dists = distancematrix(data)
    #extract distances that are from point at index "point"
    allpoints = dists[:,point]
    #extract distances that are less than search radius
    neighbourhood = allpoints[(allpoints < r)]
    #extract indices of points within search radius
    nindex_tup = np.where((allpoints<r))[0]
    nindex = np.asarray(nindex_tup)
    #create ne array with distances and related indices
    n = np.array([neighbourhood.T, nindex.T])
    n = n.T
    #sort them in ascending order and then return
    nsort = n[n[:,0].argsort()]
    return nsort[~(nsort[:,0] == 0)]

def removezerodist(dists):
    return dists[~(dists[:,0] == 0)]

def centroid(points):
    return np.array([np.mean(points[:,0]) , np.mean(points[:,1]), np.mean(points[:,2])])