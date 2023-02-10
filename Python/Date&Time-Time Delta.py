#!/bin/python3

import math
import os
import random
import re
import sys
import calendar
from datetime import date, time, timedelta, datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    # Enter your code here. Read input from STDIN. Print output to STDOUT

    # Day dd Mon yyyy hh:mm:ss +xxxx
    # Sun 10 May 2015 13:54:36 -0700
    # d = date(2005, 7, 14)
    # t = time(12, 30)
    # datetime.combine(d, t)

    wkds= ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    ymth=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    strDT1=t1
    strDT2=t2
    
    #extract 
    d1=date(int(strDT1[11:11+4]),ymth.index(strDT1[7:7+3])+1,int(strDT1[4:4+2]))
    t1=time(int(strDT1[16:16+2]),int(strDT1[19:19+2]),int(strDT1[22:22+2]))
    dt1cmb = datetime.combine(d1,t1)
    dt1_ofst_sn=strDT1[25:26]
    dt1_ofst_hr=int(strDT1[26:28])
    dt1_ofst_min=int(strDT1[28:30])
    
    d2=date(int(strDT2[11:11+4]),ymth.index(strDT2[7:7+3])+1,int(strDT2[4:4+2]))
    t2=time(int(strDT2[16:16+2]),int(strDT2[19:19+2]),int(strDT2[22:22+2]))
    dt2cmb=datetime.combine(d2,t2)
    dt2_ofst_sn=strDT2[25]
    dt2_ofst_hr=int(strDT2[26:28])
    dt2_ofst_min=int(strDT2[28:30])
    
    #adjust dates / prepare for comparison
    if dt1_ofst_sn=='-':
        dt1cmb+=timedelta(hours=dt1_ofst_hr,minutes=dt1_ofst_min)
    else:
        dt1cmb-=timedelta(hours=dt1_ofst_hr,minutes=dt1_ofst_min)

    if dt2_ofst_sn=='-':
        dt2cmb+=timedelta(hours=dt2_ofst_hr,minutes=dt2_ofst_min)
    else:
        dt2cmb-=timedelta(hours=dt2_ofst_hr,minutes=dt2_ofst_min)

    # return difference
    diff = abs(dt1cmb-dt2cmb)
    return str(int(diff.total_seconds()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
