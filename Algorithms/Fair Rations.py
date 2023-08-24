#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(B):
    lstOdd=list(filter(lambda x:x%2==1,B))
    if len(lstOdd)%2==1:
        return "NO"
    else:
        N=len(B)
        cnt=0
        for i in range(N-1):
            if B[i]%2==1:
                B[i]+=1
                B[i+1]+=1
                cnt+=2
        return str(cnt) 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(result + '\n')

    fptr.close()
