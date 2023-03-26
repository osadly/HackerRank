#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def solve(n):
    sr8np1=math.sqrt(8*n+1)
    if sr8np1 == int(sr8np1):
        if sr8np1%2==1:
            x=int((sr8np1-1)//2)
            return "Go On Bob " + str(x)
    return "Better Luck Next Time"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()
