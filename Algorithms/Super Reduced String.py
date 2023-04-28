#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    s2=s #"assamaassamaassamaassamaassamaassama"
    
    b=True
    while(b):
        b=False
        n=len(s2)
        #print(n)
        for i in range(n-1):
            if s2[i]==s2[i+1]:
                b=True
                if i<n-2:
                    s2=s2[:i]+s2[i+2:]
                else:
                    s2=s2[:i]
                break

    if s2=="":
        s2="Empty String"         
    return s2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
