#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    cs_s="abcdefghijklmnopqrstuvwxyz"
    cs=list(cs_s)
    csn=[]
    for ch in cs_s:
        n=s.count(ch)
        csn.append(n)
        
    for i in range(25):
        for j in range(i+1,26):
            if csn[i] < csn[j] or csn[i] == csn[j] and cs[i]>cs[j]:
                t1=csn[i]
                t2=cs[i]
                
                csn[i]=csn[j]
                cs[i]=cs[j]
                
                csn[j]=t1
                cs[j]=t2                
    
    print (cs[0],csn[0])
    print(cs[1],csn[1])
    print(cs[2],csn[2])
    
