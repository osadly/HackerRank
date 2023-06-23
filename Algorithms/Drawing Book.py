#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    if p==1 or p==n or (n%2==1 and p==n-1):
        return 0
    
    ffrnt=0
    if p%2==0:
        ffrnt=p/2
    else:
        ffrnt=(p-1)/2
    
    ttl=0
    if n%2==0:
        ttl=n/2
    else:
        ttl=(n-1)/2
        
    if ffrnt>ttl/2:
        return int(ttl-ffrnt)
    else:
        return int(ffrnt)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
