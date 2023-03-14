#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER p
#

def solve(d, p):
    n = int(math.sqrt(p))
    ret=0
    if d<0:
        return 0
    if d==0:
        if n*n==p:
            return 2
        else:
            return 0
    
    for i in range(n+1):
        if i * (i+d) == p:
            ret+=4
    return ret
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        d = int(first_multiple_input[0])

        p = int(first_multiple_input[1])

        result = solve(d, p)

        fptr.write(str(result) + '\n')

    fptr.close()
