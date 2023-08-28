#!/bin/python3

import math
import os
import random
import re
import sys


def serviceLane(width, cases):
    ret=[]
    for cs in cases:
        strt=cs[0]
        fnsh=cs[1]
        ret.append(min(width[strt:fnsh+1]))
 
    return ret
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(width, cases)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
