#!/bin/python3

import math
import os
import random
import re
import sys

def strangeCounter(t):
    nextMinTime=1
    tmIntrv=3
    maxTime=0
    maxValue=0

    while t > maxTime:
        maxTime=nextMinTime+tmIntrv-1
        nextMinTime=maxTime+1 
        maxValue=tmIntrv
        tmIntrv*=2
    return maxValue-(t-maxTime+(tmIntrv//2)-1)    
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
