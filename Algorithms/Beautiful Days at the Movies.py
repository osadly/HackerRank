#!/bin/python3

import math
import os
import random
import re
import sys

def beautifulDays(i, j, k):
    ret=0
    for x1 in  range(i,j+1):
        x2=int(str(x1)[::-1])
        #print(x1,x2)
        if abs(x1-x2) % k==0:
            ret+=1
    return ret
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
