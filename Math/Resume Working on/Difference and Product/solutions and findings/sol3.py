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
    else:
        lst_pairs=[]
        t = d*d + 4*p
        if t >= 0:
            scndTrm = math.sqrt(t)
            if scndTrm==int(scndTrm):
                x1=d+scndTrm
                if x1%2==0:
                    x1//=2
                    lst_pairs.append([int(x1),int(x1-d)])
                
                x2=d-scndTrm
                if x2%2==0:
                    x2//=2
                    lst_pairs.append([int(x2),int(x2-d)])
                    
                x3=-d+scndTrm
                if x3%2==0:
                    x3//=2
                    lst_pairs.append([int(x3),int(x3+d)])
                    
                x4=-d-scndTrm
                if x4%2==0:
                    x4//=2
                    lst_pairs.append([int(x4),int(x4+d)])
        
        s=set(tuple(i) for i in lst_pairs)    
        return len(list(s))

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
