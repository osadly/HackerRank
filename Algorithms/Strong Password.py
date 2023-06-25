#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    bNLUP=[False]*4
    for e in password:
        if e in numbers:
            bNLUP[0]=True
        if e in lower_case:
            bNLUP[1]=True
        if e in upper_case:
            bNLUP[2]=True
        if e in special_characters:
            bNLUP[3]=True
    
    #print(bNLUP)
    cnt=0
    for b in bNLUP:
        if b==False:
            cnt+=1
    #print(cnt)
    return cnt + max (0, 6-len(password)-cnt)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
