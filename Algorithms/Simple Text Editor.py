import sys

def processLine(s):
    tmp = s.split(' ')
    k=0
    crnt=""
    if len(ar)>0:
        crnt=ar[len(ar)-1]

    if tmp[0]=="1":
        crnt+=tmp[1]
        ar.append(crnt)
    elif tmp[0]=="2":
        k=int(tmp[1])
        crnt=crnt[:len(crnt)-k]
        ar.append(crnt)
    elif tmp[0]=="3":
        k=int(tmp[1])
        print(crnt[k-1])
    elif tmp[0]=="4":
        if len(ar)>0:
            ar.pop()
    
line = sys.stdin.readline().strip()
n=int(line)
ar = []

for i in range(n):
    line = sys.stdin.readline().strip()
    if i==0:
        ar.append("")
    processLine(line)