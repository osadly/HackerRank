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
    m1=n*(n-4*k)
    if m1 < 0:
        return n-1
    elif m1==0:
        return math.ceil(n/2)+1

    m2=math.sqrt(m1)
    i1=float((n+m2)/2)
    i2=float((n-m2)/2)

    return int( math.floor(max(i1,i2)) - math.ceil(min(i1,i2)) ) + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = solve(n, k)

        fptr.write(str(result) + '\n')

    fptr.close()
