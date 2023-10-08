#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    if s==t:
        return "Yes"
    ns=len(s)
    nt=len(t)
    if (ns==0 and k>=nt) and (nt==0 and k>=ns):
        return "Yes"

    n = min(ns, nt)
    cnt=0
    for i in range(n):
        cnt+=1
        if s[i]!=t[i]:
            cnt-=1
            break
    x = k - ((ns-cnt) + (nt-cnt))
    if x>=0 and (cnt==0 or (x%2==0) or (nt==cnt)):
        return "Yes"
    else:
        return "No"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
