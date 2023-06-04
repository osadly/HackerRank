import math
import os
import random
import re
import sys

def gridlandMetro(n, m, k, track):
    #ret=m*(n-k)
    ret=0
    trks=[]
    dictRows_Trks = {}
    rowsWthTrksLst_ALL=[]
    for i in range(k):
        #rowsWthTrksLst_ALL.add(track[i][0])
        dictRows_Trks[track[i][0]-1].append([track[i][1]-1,track[i][2]-1])
    
    #rowsWthTrksLst_Unq = list(set(rowsWthTrksLst_ALL))
        
    #rowsWthMnyTrksLst=list(rowsWthMnyTrksSet)
    #rowsUsedForTrks=len(rowsWthMnyTrksLst)
    #ret=m*(n-rowsUsedForTrks)
    print(dictRows_Trks)
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    k = int(first_multiple_input[2])
    track = []
    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)
    fptr.write(str(result) + '\n')
    fptr.close()
