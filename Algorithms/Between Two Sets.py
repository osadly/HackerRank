#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce 
#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def lstFactNum(num,lst):
    for e in lst:
        if num%e!=0:
            return False
        
    return True

def numFctrLst(num,lst):
    for e in lst:
        if e%num!=0:
            return False

    return True

def getTotalX(a, b):
    n,m=len(a),len(b)

    #a2,b2=sorted(a),sorted(b)
    mnA=min(a)
    mxB=max(b)
    ret=0
    for num in range(mnA,mxB+1):
        if lstFactNum(num,a) and numFctrLst(num,b):
            ret+=1
            
    return ret
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
