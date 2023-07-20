#!/bin/python3

import math
import os
import random
import re
import sys

def encryption(s):
    s2=""
    for e in s:
        if e!="":
            s2+=e
            
    L = len(s2)
    x = math.sqrt(L)
    rows=int(x)
    cols=int(x)+1
    if x*x == L:
        cols-=1
    if rows*cols<L:
        if rows<cols:
            cols-=1
        else:
            rows-=1
        
    #print(L,rows,cols)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
