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
#  1. INTEGER a
#  2. INTEGER b
#  3. INTEGER n
#

def solve(a, b, n):
    cnstFrMdl = int(1e+7 + 7)
    #print(cnstFrMdl)
    # any term Tn will be calculated as shown below
    # Tn = F_N * b + F_N-1 * a
    # where F_N,F_N-1 is the n & n-1 fib terms in the fib series
    # step 1 calc F_N
    # step 2 calc F_N-1
    # step 3 calc F_N * b + F_N-1 * a - return this result

    sqrt5 = math.sqrt(5)
    #print(sqrt5)
    OneOverSqrt5 = 1 / math.sqrt(5)
    #print(OneOverSqrt5)
    sqrt5Plus1Over2 = (1 + sqrt5) / 2
    #print(sqrt5Plus1Over2)
    sqrt5Minus1Over2 = (1 - sqrt5) / 2
    #print(sqrt5Minus1Over2)

    F_N = OneOverSqrt5 * ( math.pow(sqrt5Plus1Over2,n) - math.pow(sqrt5Minus1Over2,n) )
    F_N_1 = OneOverSqrt5 * ( math.pow(sqrt5Plus1Over2,n-1) - math.pow(sqrt5Minus1Over2,n-1) )
    Trm1 = (b * F_N) % cnstFrMdl
    Trm2 = (a * F_N_1) % cnstFrMdl
    CustFib_N = (Trm1 + Trm2) % cnstFrMdl
    #CustFib_N = math.fmod()
    return int(round(CustFib_N))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        n = int(first_multiple_input[2])

        result = solve(a, b, n)

        fptr.write(str(result) + '\n')

    fptr.close()
