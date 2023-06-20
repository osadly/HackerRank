#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    str1='13.09.' + str(year)
    str2='12.09.' + str(year)
    str3='26.09.' + str(year)
    
    if year == 1918:
        return str3
    if year%400 == 0:
        return str2
    if year%4 != 0:
        return str1
    if year%100 == 0:
        if year<1918:
            return str2
        else:
            return str1
    return str2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
