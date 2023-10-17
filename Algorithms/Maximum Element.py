#!/bin/python3

import math
import os
import random
import re
import sys

class Stack:
    def __init__(self):
        self.elements=[]
        
    def push(self, e):
        self.elements.append(e)
     
    def pop(self):
        del self.elements[-1]
        
    def size(self):
        return len(self.elements)
        
    def getMax(self):
        return max(self.elements)
    
def getMax(operations):
    stk = Stack() #[]
    ret = []
    crntMax = -sys.maxsize - 1
    
    bDelete=False
    for op in operations:
        if op[0]=='1':
            stk.push(int(op.split(' ')[1]))
            crntMax = max(crntMax, stk.elements[len(stk.elements)-1])
        elif op[0]=='2':
            bDelete=True
            stk.pop()
        else:
            if bDelete:
                crntMax=stk.getMax()
                bDelete=False
            ret.append(crntMax)
    return ret
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
