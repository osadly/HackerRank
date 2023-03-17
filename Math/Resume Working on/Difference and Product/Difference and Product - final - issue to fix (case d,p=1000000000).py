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
    if d==0 and p==0:
        return 1
    elif p==0:
        return 2
    elif d==0:
        n=int(math.sqrt(p))
        if n*n==p:
            return 2
        else:
            return 0
    else:
        b,c=d,-1*p
        if b*b-4*1*c >= 0:
            t=math.sqrt(b*b-4*1*c)
            if int(t) != t:
                return 0
            t=int(t)
            lst_pairs=[]
            if (-1*b + t)%2==0:
                x=int ((-1*b + t)//2)
                if x!=0 and p%x==0:
                    y=int(p//x)
                    lst_pairs.append([x,y])
            if (-1*b - t)%2==0:
                x=int ((-1*b - t)//2)
                if x!=0 and p%x==0:
                    y=int(p//x)
                    lst_pairs.append([x,y])
            if (b + t)%2==0:
                x=int ((b + t)//2)
                if x!=0 and p%x==0:
                    y=int(p//x)
                    lst_pairs.append([x,y])
            if (b - t)%2==0:
                x=int ((b - t)//2)
                if x!=0 and p%x==0:
                    y=int(p//x)
                    lst_pairs.append([x,y])
            
    s=set(tuple(i) for i in lst_pairs)
    print(lst_pairs)
    return len(list(s)) 

d,p=1000000000,2
print(d,p,solve(d,p))
d,p=1000000000,1000000000
print(d,p,solve(d,p))
d,p=0,4
print(d,p,solve(d,p))
d,p=-1,1
print(d,p,solve(d,p))
d,p=30,40
print(d,p,solve(d,p))
d,p=12,0
print(d,p,solve(d,p))
d,p=23,50
print(d,p,solve(d,p))
d,p=3,18
print(d,p,solve(d,p))
d,p=0,0
print(d,p,solve(d,p))
d,p=0,1
print(d,p,solve(d,p))
d,p=0,2
print(d,p,solve(d,p))
d,p=1,0
print(d,p,solve(d,p))
d,p=1,1
print(d,p,solve(d,p))
d,p=1,2
print(d,p,solve(d,p))
d,p=2,0
print(d,p,solve(d,p))
d,p=2,1
print(d,p,solve(d,p))
d,p=2,2
print(d,p,solve(d,p))

