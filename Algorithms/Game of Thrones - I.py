#!/bin/python3

import math
import os
import random
import re
import sys

def gameOfThrones(s):
    ar=[0]*26
    orda=ord('a')
    for i in range(len(s)):
        ar[ord(s[i])-orda]+=1
        
    cntV,cntO=0,0
    for i in range(26):
        if ar[i]%2==0:
            cntV+=1
        else:
            cntO+=1
            
    if (len(s)%2==0 and cntO==0) or (len(s)%2!=0 and cntO==1):
        return "YES"
    else:
        return "NO"
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
