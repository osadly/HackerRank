#!/bin/python3

import math
import os
import random
import re
import sys

def chocolateFeast(n, c, m):
    bars1=n//c
    wraps=bars1
    bars2=[wraps//m]
    i=0
    while bars2[i]>=1:
        wraps=wraps%m+bars2[i]
        bars2.append(wraps//m)
        i+=1
    return bars1+sum(bars2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
