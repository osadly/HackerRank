#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
    #arr=[2,1,2]
    cnt=0
    i=0
    n=len(arr)
    #k=min(k,n)
    while i < n-1 and cnt<k:
        mx=max(arr[i+1:])
        
        if mx>arr[i]:
            mxIdx=arr.index(mx)
            arr[mxIdx],arr[i]=arr[i],arr[mxIdx]
            cnt+=1
        i+=1

    print(arr)
        
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
