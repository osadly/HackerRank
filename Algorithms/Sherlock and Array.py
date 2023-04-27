#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    n=len(arr)
    sm=sum(arr)

    sarL = [0] * n
    sarL[n-1] = sm-arr[n-1]

    sarR = [0] * n
    sarR[0] = sm-arr[0]

    for i in range(n):
        if i>0 and i<n-1:
            sarL[i]=sarL[i-1]+arr[i-1]
            sarR[i]=sarR[i-1]-arr[i]
            
        if sarL[i]==sarR[i]:
            return "YES"
        
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
