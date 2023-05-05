#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

def twoStacks(maxSum, a, b):
    crntSum=0
    bCont=True
    ret=0
    idxA,idxB=0,0
    n,m=len(a),len(b)
    
    while (maxSum>crntSum):
        if idxA<n-1 and a[idxA]<=b[idxB]:
            crntSum+=a[idxA]
            idxA+=1
        elif idxB<m-1:
            crntSum+=b[idxB]
            idxB+=1
        else:
            bCont=False
        
        if maxSum>=crntSum:
            ret+=1
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
