#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    lnS=len(s)
    ordS=[]
    for i in range(len(s)-1):
        ordS.append(abs(ord(s[i+1])-ord(s[i])))
        
    for i in range(len(ordS)//2):
        if ordS[i] != ordS[len(ordS)-i-1]:
            return "Not Funny"

    return "Funny"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
