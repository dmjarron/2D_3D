# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 13:55:56 2017
Code module design to use Principal Component Analysis
to classify points into different feature types based on
the neighbourhood characteristics.  This codes focus is
finding linear features.  Needs to be edited in the future
to include support for different data structures (KD tree, octree, etc.)
Input: textfile of all 3D points, unstructured
Output: Vector of all points classified as a linear feature
@author: David Jarron, 10/10/2017
"""
# !/usr/bin/python

import numpy as np
import nsearch as ns
from sklearn.neighbors import KDTree
# load data and convert to matrix format
cloud = np.random.random((1000,3)) * 1000
N = len(cloud)

#search radius
R = 200.0

treecloud = KDTree(cloud, metric = 'euclidean')

adjMatrix = np.zeros((N,N))
i = 0
p = cloud[0]
#    find nearest neighbours of current point
ind = treecloud.query_radius(p, r = 200)
neighbours = cloud[ind[0]]
#   generate the dispersion matrix 
C = ns.centroid(neighbours)
dispmatrix = np.dot((neighbours - C), (neighbours - C).T)
#   Perform eigenvalue decomposition on dispersion matrix to find
#   principal components
w, v = np.linalg.eig(dispmatrix)
#eigenvale / vectors extracted, still need to reduce them to real numbers