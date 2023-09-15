import math
import os
import random
import re
import sys

def palindromeIndex(s):
    n=len(s)
    m=n//2
    for i in range(m):
      if s[i]!=s[n-i-1]:
          if s[i]==s[n-i-2] and s[i+1]==s[n-i-3]:
              return n-i-1
          else:
              return i
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
