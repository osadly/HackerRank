#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations


def solve(s):
    lnS=len(s)
    result=[]
    for i in range(1,lnS+1):
        comb = combinations(s,i)
        for e in comb:
            lst=list(e)
            result.append(''.join(lst))
    return sorted(result) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = input()

        result = solve(s)

        fptr.write('\n'.join(result))
        fptr.write('\n')

    fptr.close()
