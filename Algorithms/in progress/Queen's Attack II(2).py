#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    ret=0
    #print(n, k, r_q, c_q,obstacles)
    #1) left
    for i in range(r_q-1,0,-1):
        if [i,c_q] in obstacles:
            break
        ret+=1
    #print(ret)
    #2) right
    for i in range(r_q+1,n+1):
        if [i,c_q] in obstacles:
            break
        ret+=1
    #print(ret)
    #3) left-up
    i,j=r_q-1,c_q+1
    while i>=1 and j<=n and [i,j] not in obstacles:
        ret+=1
        i-=1
        j+=1
    
    #4) right-up
    i,j=r_q+1,c_q+1
    while i<=n and j<=n and [i,j] not in obstacles:
        ret+=1
        i+=1
        j+=1
    
    #5) right-down
    i,j=r_q+1,c_q-1
    while i<=n and j>=1 and [i,j] not in obstacles:
        ret+=1
        i+=1
        j-=1
    
    #6) left-down
    i,j=r_q-1,c_q-1
    while i>=1 and j>=1 and [i,j] not in obstacles:
        ret+=1
        i-=1
        j-=1
    
    #7) up
    for j in range(c_q-1,0,-1):
        if [r_q,j] in obstacles:
            break
        ret+=1
    
    #8) down
    for j in range(c_q+1,n+1):
        if [r_q,j] in obstacles:
            break
        ret+=1
    
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
