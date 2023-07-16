#!/bin/python3

import math
import os
import random
import re
import sys

def power_modulo(base, exponent, modulo):
    result = 1
    base %= modulo

    while exponent > 0:
        # If the current bit of the exponent is 1, multiply the result with the base
        if exponent & 1:
            result = (result * base) % modulo

        # Double the base and reduce it modulo to keep it within range
        base = (base * base) % modulo

        # Move to the next bit of the exponent
        exponent >>= 1
    return result
def solve(a):
    x=int(1e9 + 7)
    nTotal=len(a)
    nEven,nOdd=0,0

    for e in a:
        if e%2==0:
            nEven+=1

    nOdd = nTotal-nEven
    
    print(a)
    ret1=int(power_modulo(2,nEven,x)-1)
    #print("nEven=",nEven,",x=",x,",power_modulo(2,nEven,x)-1=",power_modulo(2,nEven,x)-1,",Expected is",int(math.pow(2,nEven)-1))
    
    ret2=int(((power_modulo(2,nOdd-1,x))-1))
    #print("nOdd=",nOdd,",x=",x,",int(((power_modulo(2,nOdd-1,x))-1))=",int(((power_modulo(2,nOdd-1,x))))-1)
    
    ret3=int((ret1*ret2) % x)
    print(ret1,ret2)
    ret=int ( ( int ((ret1+ret2) % x) + ret3 ) % x )
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)
    #result = solve([1,2,2])

    fptr.write(str(result) + '\n')

    fptr.close()
