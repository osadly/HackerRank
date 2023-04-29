#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY A
#  2. INTEGER_ARRAY B
#


def beautifulPairs(A, B):
  nA=[0]*1001
  nB=[0]*1001
  n=len(A)
  for i in range(n):
    nA[A[i]]+=1
    nB[B[i]]+=1

  ret=0
  for i in range(1001):
    ret+=min(nA[i],nB[i])
  if ret==n:
    return ret-1
  else:
    return ret+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = beautifulPairs(A, B)

    fptr.write(str(result) + '\n')

    fptr.close()
