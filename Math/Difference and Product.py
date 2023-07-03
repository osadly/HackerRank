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
    #There are no pairs of integers with absolute difference -1, because the absolute value is never negative.
    if d<0:
        return 0
    elif d==0:
        if p<0:
            return 0
        elif p==0:
            return 1
        elif p > 0:
            x1 = int(math.sqrt(p)) * int(math.sqrt(p))
            x2 = math.sqrt(p) * math.sqrt(p)
            if x1 == x2:
                return 2
            else:
                return 0
    else:
        ausr = d*d+4*p
        #print("ausr=",ausr)
        if ausr == 0:
            return 2
        elif ausr < 0:
            return 0
        elif ausr > 0:
            x1 = math.sqrt(ausr)
            if int(x1+0.5)**2==ausr:
                return 4
            else:
                return 0

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
