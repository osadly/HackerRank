#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    #s='abbcccaabbbbxzzzz'
    orda=ord('a')
    arSubStr=[]
    for i in range(len(s)):
        if i>0 and s[i]==s[i-1]:
            tmp=len(arSubStr)
            arSubStr[tmp-1]+=s[i]
        else:
            arSubStr.append(s[i])

    arSubStrMax=[0]*26
    for e in arSubStr:
        idx=ord(e[0])-orda
        arSubStrMax[idx]=max(arSubStrMax[idx],len(e))
        
    #for i in range(len(arSubStrMax)):
    #    if arSubStrMax[i]>0:
    #        arSubStrMax[i]*=(i+1)
    
    print(arSubStr,arSubStrMax)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
