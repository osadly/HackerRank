#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

    
def bfs(n, m, edges, s):
    allNodesEdgeList = [[] for i in range(n)]

    for edg in edges:
        allNodesEdgeList[edg[0]-1].append(edg[1]-1)
        allNodesEdgeList[edg[1]-1].append(edg[0]-1)
        
    visitedNodes=[False]*n
    visitedNodes[s-1]=True

    que = [s-1]

    ret = [-1]*n
    ret[s-1]=0

    while len(que)>0:
        crntNd=que.pop(0)
        nbrsCrntNd = allNodesEdgeList[crntNd]

        for j in range(len(nbrsCrntNd)):
            if not visitedNodes[nbrsCrntNd[j]]:
                visitedNodes[nbrsCrntNd[j]]=True
                que.append(nbrsCrntNd[j])
                ret[nbrsCrntNd[j]]=6+ret[crntNd]
                
    ret.remove(0)
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
