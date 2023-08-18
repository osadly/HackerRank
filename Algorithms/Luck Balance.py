#!/bin/python3

import math
import os
import random
import re
import sys

def luckBalance(k, contests):
    #print(k)
    #print(contests)
    arr=[]
    ret=0
    for i in range(len(contests)):
        if contests[i][1]==0:
            ret+=contests[i][0]
        else:
            arr.append(contests[i][0])
            
    arr=sorted(arr)
    '''
    # solution 1
    for i in range(len(arr)):
        if i<len(arr)-k:
            ret-=arr[i]
        else:
            ret+=arr[i]
    return ret
    '''
    '''
    # solution 2
    arr=arr[::-1]
    #print(arr)
    ret+=sum(arr[:k])
    ret-=sum(arr[k:])
    '''
    # solution 3
    k2=max(0,len(arr)-k)
    ret-=sum(arr[:k2])
    ret+=sum(arr[k2:])
    
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
