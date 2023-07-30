#!/bin/python3

import math
import os
import random
import re
import sys

def repeatedString(s, n):
    m = len(s)
    ret=s.count('a')*(n//m)
    x=n%m
    if x>0:
        ret+=s[:x].count('a')
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
