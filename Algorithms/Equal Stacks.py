#!/bin/python3

import math
import os
import random
import re
import sys
                
def equalStacks(h1, h2, h3):
    hr=[list(reversed(h1)),list(reversed(h2)),list(reversed(h3))]
    smArR=[sum(hr[0]),sum(hr[1]),sum(hr[2])]

    ret=0
    maxSum = max(smArR)
    maxSumIdx = smArR.index(max(smArR))
    minSum = min(smArR)
    minSumIdx = smArR.index(min(smArR))

    print(smArR)
    while maxSum > minSum:
        x=hr[maxSumIdx].pop()
        smArR[maxSumIdx] -= x
        maxSum = max(smArR)
        maxSumIdx = smArR.index(max(smArR))
        minSum = min(smArR)
        minSumIdx = smArR.index(min(smArR))
        print(smArR)
    return smArR[0]            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
