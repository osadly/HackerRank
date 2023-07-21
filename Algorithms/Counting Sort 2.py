import math
import os
import random
import re
import sys

def countingSort(arr):
    tmp=[0]*100
    for e in arr:
        tmp[e]+=1
    
    ret=[]
    for k in range(len(tmp)):
        for i in range(tmp[k]):
            ret.append(k)
    
    return ret

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
