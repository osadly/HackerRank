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
#  1. INTEGER n
#  2. INTEGER k
#

def solve(n, k):
    ret= int(math.factorial(k+n-1)//math.factorial(k)//math.factorial(n-1))
    return int(ret%1000000000)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        k = int(input().strip())

        result = solve(n, k)
        
        fptr.write(str(result) + '\n')

    fptr.close()
