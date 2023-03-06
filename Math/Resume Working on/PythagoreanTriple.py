#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pythagoreanTriple' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER a as parameter.
#

def pythagoreanTriple(a):
    k=0
    if a%2==1:
        k=int((a*a-1)/2)
        b=int(k)
        c=int(k+1)
        return [a,b,c]
    else:
        t=int((a-2)/2)
        s=int((a+2)/2)
        b=int(s*t)
        c=int((s*s+t*t)/2)
        return [a,b,c]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = int(input().strip())

    triple = pythagoreanTriple(a)
    #triple = pythagoreanTriple(int(1e9-1))

    fptr.write(' '.join(map(str, triple)))
    fptr.write('\n')

    fptr.close()
