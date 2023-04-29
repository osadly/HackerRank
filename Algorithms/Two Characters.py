#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def validate(sTmp):
  #print(sTmp)
  n=len(sTmp)
  for i in range(n-1):
    if sTmp[i]==sTmp[i+1]:
      return 0
  return n
  
def alternate(s):
  ret=0
  for i in range(ord('a'),ord('z')+1):
    ch1=chr(i)
    pos1=s.find(ch1)
    if pos1>=0:
      for j in range(ord('a'),ord('z')+1):
        if i!=j:
          ch2=chr(j)
          pos2=s.find(ch2)
          if pos2>=0: #and pos1<pos2:
            sTmp=''
            for eCh in s:
              if eCh == ch1 or eCh == ch2:
                sTmp += eCh
            ret = max(validate(sTmp), ret)
  
  return ret
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
