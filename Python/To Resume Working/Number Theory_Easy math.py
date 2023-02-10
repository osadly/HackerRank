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
# The function accepts INTEGER x as parameter.
#

def solve(x):
    total_cnt_digits=len(str(x))
    b=True
    nF=0
    while b:
        for cnt_frs in range(1,total_cnt_digits+1):
            cnt_zrs = total_cnt_digits - cnt_frs
            strF = cnt_frs*'4' + cnt_zrs*'0'
            nF=int(strF)
                
            if nF%x==0 and nF/x>0:
                b=False
                break
        
        if not b:
            break
        total_cnt_digits+=1

    nF=0
    nZ=0
    for i in range(len(strF)):
        if strF[i]=='4':
            nF+=1
        else:
            nZ+=1
    
    return 2*nF+nZ

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        x = int(input().strip())

        result = solve(x)

        fptr.write(str(result) + '\n')

    fptr.close()
