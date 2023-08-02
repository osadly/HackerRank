#!/bin/python3

import math
import os
import random
import re
import sys

def jumpingOnClouds(c):
    n=len(c)
    i=0
    cnt=0
    while i < n-1:
        if c[i]==0 and (i+2<=n-1 and c[i+2]==0):
            i+=2
        else:
            i+=1
            
        cnt+=1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
