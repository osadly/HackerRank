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
        ap2=int(a*a)
        ap2_1=int(ap2-1)
        k=int(ap2_1//2)     # use // instead of / to get accurate results
        b=int(k)
        c=int(k+1)
        return [a,b,c]
    else:
        t=int((a-2)//2)     # use // instead of / to get accurate results
        s=int((a+2)//2)     # use // instead of / to get accurate results
        b=int(s*t)
        c=int((s*s+t*t)//2) # use // instead of / to get accurate results
        return [a,b,c]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = int(input().strip())

    triple = pythagoreanTriple(a)
    #triple = pythagoreanTriple(int(1e9-1))

    fptr.write(' '.join(map(str, triple)))
    fptr.write('\n')

    fptr.close()
