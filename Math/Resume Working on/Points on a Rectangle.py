#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY coordinates as parameter.
#

def newLine(pt1,pt2):
    ln=[]
    ln.append((pt2[1]-pt1[1])/(pt2[0]-pt1[0]))
    ln.append((pt1[0]*pt2[1]-pt2[0]*pt1[1]) / (pt1[0]-pt2[0]))
    return ln
    
def solve(coordinates):
    if len(coordinates)<4:
        return 'YES'
    xs,ys=[],[]
    for i in range(len(coordinates)):
        xs.append(coordinates[i][0])
        ys.append(coordinates[i][1])

    xMinMax=[min(xs),max(xs)]
    yMinMax=[min(ys),max(ys)]
    
    corners=[]
    for ix in range(2):
        for iy in range(2):
            corners.append([xMinMax[ix],yMinMax[iy]])
            
    lns=[]
    for i in range(len(corners)-1):
        for j in range(i+1,len(corners)):
            if corners[i][0]==corners[j][0] and corners[i][1]==corners[j][1]:
                lns.append(newLine(corners[i],corners[j]))
    print(lns)            
    # next step - is to fix bug - when divide by zero in the newLine function
    # continue from here - check other points on any of four lines/lns 
    
    return 'YES'