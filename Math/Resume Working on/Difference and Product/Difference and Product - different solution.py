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
    if d<0:
        return 0
    b,c=d,-1*p
    t=math.sqrt(b*b-4*1*c)
    if int(t) != t:
        return 0
    t=int(t)
    lst_pairs=[]
    if (-1*b + t)%2==0:
        x=int ((-1*b + t)//2)
        if p%x==0:
            y=int(p//x)
            lst_pairs.append([x,y])
    if (-1*b - t)%2==0:
        x=int ((-1*b - t)//2)
        if p%x==0:
            y=int(p//x)
            lst_pairs.append([x,y])
    if (b + t)%2==0:
        x=int ((b + t)//2)
        if p%x==0:
            y=int(p//x)
            lst_pairs.append([x,y])
    if (b - t)%2==0:
        x=int ((b - t)//2)
        if p%x==0:
            y=int(p//x)
            lst_pairs.append([x,y])
            
    s=set(tuple(i) for i in lst_pairs)
    #print(lst_pairs)
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