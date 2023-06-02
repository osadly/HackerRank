#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridlandMetro' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER k
#  4. 2D_INTEGER_ARRAY track
#

def gridlandMetro(n, m, k, track):
    #ret=m*(n-k)
    ret=0
    trks=[]
    rowsWthTrksLst_ALL=[]
    dictRows_TrksCnt = {}
    for i in range(k):
        rowsWthTrksLst_ALL.add(track[i][0])
        dictRows_TrksCnt[track[i][0]]+=1
    
    rowsWthTrksLst_Unq = list(set(rowsWthTrksLst_ALL))
        
    rowsWthMnyTrksLst=list(rowsWthMnyTrksSet)
    rowsUsedForTrks=len(rowsWthMnyTrksLst)
    ret=m*(n-rowsUsedForTrks)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()
