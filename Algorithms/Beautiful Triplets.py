import math
import os
import random
import re
import sys

def beautifulTriplets(d, arr):
    n = len(arr)
    cnt=0
    for i in range(n-1):
        if arr[n-1] >= arr[i] + 2*d:
            if ((arr[i] + d) in arr) and ((arr[i] + 2*d) in arr):
                cnt+=1
            
    return cnt
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
