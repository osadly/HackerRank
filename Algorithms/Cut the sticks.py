#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    srtdArr=sorted(arr)
    #dct={}
    n=len(srtdArr)
    ret=[n]
    sbtrct=0
    mn=srtdArr[0]
    for i in range(n):
        if srtdArr[i]==mn:
            sbtrct+=1
        else:
            n-=sbtrct
            ret.append(n)
            sbtrct=1
            mn=srtdArr[i]
    return ret
        
        
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
