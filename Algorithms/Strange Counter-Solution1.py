#!/bin/python3

import math
import os
import random
import re
import sys

def strangeCounter(t):
    minTime=1
    tmIntrv=3
    maxTime=minTime+tmIntrv-1
    timing=[0]
    maxValues=[0]
    while minTime<=int(1e12):
        timing.append(maxTime)
        maxValues.append(tmIntrv)
        tmIntrv*=2
        minTime=maxTime+1
        maxTime=minTime+tmIntrv-1
    #print(timing,maxValues)
    n=len(maxValues)
    for i in range(n):
        if t<=timing[i]:
            return maxValues[i]-(t-timing[i-1]-1)
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
