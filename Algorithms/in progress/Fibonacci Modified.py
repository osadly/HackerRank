#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fibonacciModified' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
#

def fibonacciModified(t1, t2, n):
    #lpn=int(1e9)+7
    fib=[n]*n
    fib[0], fib[1]=t1, t2
    for i in range(2, n):
        fib[i] = (fib[i-2] + (fib[i-1]*fib[i-1]))
    #fib[n-1]=fib[n-3]%lpn + (fib[n-2]%lpn*fib[n-2]%lpn)
    return fib[n-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    t1 = int(first_multiple_input[0])

    t2 = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
