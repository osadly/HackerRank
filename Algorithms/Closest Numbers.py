#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    srtdAr = sorted(arr) #[::-1]
    #print(srtdAr)
    minDf = int(2*1e7 + 1)
    ret=[]
    n = len(srtdAr)
    for i in range(n-1):
        crntDf=srtdAr[i+1]-srtdAr[i]
        if crntDf < minDf:
            ret.clear()
            ret.append(i)
            minDf=crntDf
        elif crntDf == minDf:
            ret.append(i)
    fnl=[]    
    for i in range(len(ret)):
        fnl.append(srtdAr[ret[i]])
        fnl.append(srtdAr[ret[i]+1])
             
    return fnl
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
