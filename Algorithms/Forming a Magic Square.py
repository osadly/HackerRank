#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    trgt=[]
    trgt.append([[8,1,6],[3,5,7],[4,9,2]])
    trgt.append([[6,1,8],[7,5,3],[2,9,4]])
    trgt.append([[2,7,6],[9,5,1],[4,3,8]])
    trgt.append([[4,3,8],[9,5,1],[2,7,6]])
    trgt.append([[2,9,4],[7,5,3],[6,1,8]])
    trgt.append([[4,9,2],[3,5,7],[8,1,6]])
    trgt.append([[8,3,4],[1,5,9],[6,7,2]])
    trgt.append([[6,7,2],[1,5,9],[8,3,4]])
    
    minCost = sys.maxsize
    
    for i in range(8):
        crntCost=0
        for j in range(3):
            for k in range(3):
                crntCost += abs(trgt[i][j][k] - s[j][k])
                #print(trgt[i][j][k] - s[j][k])
        minCost = min(minCost,crntCost)
        #print("minCost=", minCost)

    return minCost
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
