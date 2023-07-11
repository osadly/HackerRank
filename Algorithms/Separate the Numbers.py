#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#
def buildStrToCmp(tmp,n):
    x=int(tmp)
    #ai=[x]
    
    fnl=tmp
    while len(fnl)<n:
        x+=1
        fnl+=str(x)
        #ai.append(x)
    return fnl

def separateNumbers(s):
    lnS=len(s)
    if lnS==1 or s[0]=='0':
        print("NO")
        return
        
    for i in range(1,int(lnS/2)+1):
        tmp=s[0:i]
        refStr = buildStrToCmp(tmp,lnS)
        if refStr==s:
            print("YES",tmp)
            return
            
    print("NO")
    return

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
