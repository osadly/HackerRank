#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
  m=len(c)
  if n==m:
    return 0

  cSrtd=sorted(c)
  dst=[]

  for i in range(len(cSrtd)-1):
    dst.append(cSrtd[i+1]-cSrtd[i])

  if len(dst)>0:
    ret=max(max(dst)//2,cSrtd[0],n-1-cSrtd[m-1])
  else:
    ret=max(cSrtd[0],n-1-cSrtd[0])

  return ret #(mx//2 + mx%2)
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
