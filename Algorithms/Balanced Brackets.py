#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    n=len(s) 
    if n%2==1:
        return "NO"
    
    #dct1={'(' : ')' , '[' : ']', '{' : '}'}
    dct={ ")" : "(","]":"[", "}":"{" }
    lst=[]
    for e in s:
        if e in "{[(":
            lst.append(e)
        else:
            if len(lst)==0:
                return "NO"
            elif lst[len(lst)-1] != dct[e]:
                return "NO"
            else:
                lst.pop(len(lst)-1)
    if len(lst)==0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
