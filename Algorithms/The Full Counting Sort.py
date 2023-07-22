#!/bin/python3

import math
import os
import random
import re
import sys


def countSort(arr):
    n=len(arr)
    m=n//2
    for i in range(m):
        arr[i][1]="-"
    result = [""] * n
    for i in range(n):
        idx=int(arr[i][0])
        result[idx]+=" " + arr[i][1]
    print(''.join(result)[1:])
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
