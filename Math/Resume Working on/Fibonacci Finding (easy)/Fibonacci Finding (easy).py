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
    # any term Tn will be calculated as shown below
    # Tn = F_N-1 * b + F_N-2 * a
    # where F_N-1,F_N-2 is the n-1 & n-2 fib terms in the fib series 
    # step 1 calc F_N-1
    # step 2 calc F_N-2
    # step 3 calc F_N-1 * b + F_N-2 * a - return this result
    
    sqrt5=math.sqrt(5)
    invSqrt5=1/math.sqrt(5)
    
    
    for i in (a,b)
    
    

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
