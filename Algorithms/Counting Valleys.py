#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    arr=[]
    crnt=0
    for i in range(steps):
        if path[i]=='D':
            crnt-=1
            arr.append(crnt)
        else:
            crnt+=1
            arr.append(crnt)

    ret=0
    bVal=False
    for i in range(len(arr)):
        if bVal==False and arr[i]<0:
            ret+=1
            bVal=True
        elif arr[i]>=0:
            bVal=False
        
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
