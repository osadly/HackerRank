#!/bin/python3

import math
import os
import random
import re
import sys

def viralAdvertising(n):
    shared=[0]*n
    shared[0]=5
    liked,cumulative=[0]*n,[0]*n
    for i in range(n-1):
        liked[i]=int(shared[i]/2)
        if i>0:
            cumulative[i]=liked[i]+cumulative[i-1]
        else:
            cumulative[i]=liked[i]
        shared[i+1]=liked[i]*3
        
    liked[n-1]=int(shared[n-1]/2)
    cumulative[n-1]=liked[n-1]+cumulative[n-2]
    print(shared,liked,cumulative)
        
    return cumulative[n-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
