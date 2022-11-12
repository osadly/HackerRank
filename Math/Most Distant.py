#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts 2D_INTEGER_ARRAY coordinates as parameter.
#

def solve(coordinates):
    Xs,Ys=[],[]
    for i in range(len(coordinates)):
        if(coordinates[i][0]!=0):
            Xs.append(coordinates[i][0])
        else:
            Ys.append(coordinates[i][1])
            
    xMn = float(min(Xs))
    xMx = float(max(Xs))
    yMn = float(min(Ys))
    yMx = float(max(Ys))
    
    ds=[]
    ds.append(float(xMx-xMn))
    ds.append(float(yMx-yMn))
    ds.append(float(math.sqrt(xMn*xMn + yMn*yMn)))
    ds.append(float(math.sqrt(xMn*xMn + yMx*yMx)))
    ds.append(float(math.sqrt(xMx*xMx + yMn*yMn)))
    ds.append(float(math.sqrt(xMx*xMx + yMx*yMx)))
    return max(ds)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = solve(coordinates)

    fptr.write(str(result) + '\n')

    fptr.close()
