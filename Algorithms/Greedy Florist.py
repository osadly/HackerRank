#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    cSrtd=sorted(c)
    cSrtd.reverse()
    n=len(cSrtd)
    if k==n:
        return sum(cSrtd)
    if k>n:
        return sum(cSrtd[:k])
    
    x=n//k
    y=n%k
    ret=0
    cnt=1
    for i in range(0,x*k,k):
        ret+=sum(cSrtd[i:i+k]) * cnt
        cnt+=1
        
    ret+=sum(cSrtd[x*k:n]) * cnt
                
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
