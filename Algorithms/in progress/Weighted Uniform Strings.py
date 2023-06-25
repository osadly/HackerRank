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
    #alpha='abcdefghijklmnopqrstuvwxyz'
    orda=ord('a')

    wts=[]
    for i in range(len(s)):
        ch=s[i]
        if i>0 and ch==s[i-1]:
                x=wts[len(wts)-1]
                wts.append(x+ord(ch)-orda+1)
        else:
            wts.append(ord(ch)-orda+1)
    
    for q in queries:
        if wts.find(q):
            print("Yes")
    

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
