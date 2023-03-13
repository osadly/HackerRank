#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. LONG_INTEGER a
#  2. LONG_INTEGER b
#  3. LONG_INTEGER x
#  4. LONG_INTEGER y
#

def gcd(a,b):
    if a==b:
        return a
    if a==1 or b==1:
        return 1
        
    w=max(a,b)
    z=min(a,b)
    
    while True:
        w-=z
        if w==z:
            return w
            
        if w==1 or z==1:
            return 1

        if z>w:
            t=w
            w=z
            z=t
    


def solve(a, b, x, y):
    m=gcd(a,b)
    if x%m==0 and y%m==0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a=[3299,2584,968,7545,5564,1595,3144,3627,8375,7913]
        b=[7314,2065,1238,2436,1059,4472,2372,4710,5848,5387]
        x=[6015,5206,91,3299,4129,8536,1788,9834,182,3397]
        y=[6906,6088,9293,4059,3475,7035,1197,6925,958,8880]

        for i in range(len(a)):
            result = solve(a[i], b[i], x[i], y[i])

