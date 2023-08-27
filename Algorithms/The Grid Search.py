import math
import os
import random
import re
import sys

def gridSearch(G, P):
    R=len(G)
    C=len(G[0])
    for i in range(R-len(P)+1):
        for j in range(C-len(P[0])+1):
            ti,tj=i,j
            pi,pj=0,0
            while G[ti][tj]==P[pi][pj]:
                tj+=1
                pj+=1
                if pj>len(P[0])-1:
                    ti+=1
                    pi+=1
                    tj=j
                    pj=0
                    
                    if pi>len(P)-1:
                        return "YES"
                        
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
