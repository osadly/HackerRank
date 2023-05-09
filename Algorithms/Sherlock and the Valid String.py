#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    ordA=ord('a')
    lst=[0]*26
    for i in range(26):
        lst[i]=s.count(chr(ordA+i))
    
    lst2=list(filter(lambda x:x>0,lst))
    hlp_set=set(lst2)
    
    if len(hlp_set)>2:
        return 'NO'

    if len(hlp_set)==1:
        return 'YES'
        
    if len(hlp_set)==2:
        x_min=min(hlp_set)
        x_max=max(hlp_set)
        
        if x_max-x_min == 1 and (lst2.count(x_max)==1 or lst2.count(x_min)==1):
            return 'YES'
        elif x_min==1 and lst2.count(x_min)==1:
            return 'YES'
        else:
            return 'NO'
        
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
