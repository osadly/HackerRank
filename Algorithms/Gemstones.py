#!/bin/python3

import math
import os
import random
import re
import sys

def gemstones(arr):
    x=ord('a')
    ret=26
    for i in range(26):
        for j in range(len(arr)):
            if chr(x+i) not in arr[j]:
                ret-=1
                break
            
    return ret
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
