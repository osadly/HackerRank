import math
import os
import random
import re
import sys

def queensAttack(n, k, r_q, c_q, obstacles):
    print("obstacles:",obstacles)
    cnt=min(r_q-1,c_q-1)+min(n-r_q,c_q-1)+2*(n-1)+min(n-r_q,n-c_q)+min(r_q-1,n-c_q)
    
    vals=[-1]*8
    for i in range(len(obstacles)):
        if obstacles[i][0]==r_q and obstacles[i][1]<c_q:
            if vals[0]==-1:
                vals[0]=obstacles[i][1]
            else:
                vals[0]=max(obstacles[i][1],vals[0])
                
        elif obstacles[i][0]==r_q and obstacles[i][1]>c_q:
            if vals[1]==-1:
                vals[1]=obstacles[i][1]
            else:
                vals[1]=min(obstacles[i][1],vals[1])
                    
        elif obstacles[i][1]==c_q and obstacles[i][0]>r_q:
            if vals[2]==-1:
                vals[2]=obstacles[i][0]
            else:
                vals[2]=min(obstacles[i][0],vals[2])
                
        elif obstacles[i][1]==c_q and obstacles[i][0]<r_q:
            if vals[3]==-1:
                vals[3]=obstacles[i][0]
            else:
                vals[3]=max(obstacles[i][0],vals[3])

        elif obstacles[i][0]-r_q==c_q-obstacles[i][1] and obstacles[i][0]>r_q:
            if vals[4]==-1:
                vals[4]=obstacles[i][0]
            else:
                vals[4]=min(obstacles[i][0],vals[4])

        elif obstacles[i][0]-r_q==c_q-obstacles[i][1] and obstacles[i][0]<r_q:
            if vals[5]==-1:
                vals[5]=obstacles[i][0]
            else:
                vals[5]=max(obstacles[i][0],vals[5])
        
        elif obstacles[i][0]-r_q==obstacles[i][1]-c_q and obstacles[i][0]>r_q:
                if vals[6]==-1:
                    vals[6]=obstacles[i][0]
                else:
                    vals[6]=min(obstacles[i][0],vals[6])
    
        elif obstacles[i][0]-r_q==obstacles[i][1]-c_q and obstacles[i][0]<r_q:
                if vals[7]==-1:
                    vals[7]=obstacles[i][0]
                else:
                    vals[7]=max(obstacles[i][0],vals[7])
                    
    print(vals)
    if vals[0]!=-1:
        cnt-=vals[0]
    if vals[1]!=-1:
        cnt-=(n-vals[1]+1)
    if vals[2]!=-1:
        cnt-=(n-vals[2]+1)
    if vals[3]!=-1:
        cnt-=vals[3]
    if vals[4]!=-1:
        cnt-=(n-vals[4]+1)
    if vals[5]!=-1:
        cnt-=vals[5]
    if vals[6]!=-1:
        cnt-=(n-vals[6]+1)
    if vals[7]!=-1:
        cnt-=vals[7]
                                    
    return cnt
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    #n,k,r_q,c_q=8, 1, 4, 4
    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    #obstacles = []
    #n,k,r_q,c_q=8, 1, 4, 4
    result = queensAttack(n, k, r_q, c_q, obstacles)
    #result = queensAttack(8, 1, 4, 4, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
