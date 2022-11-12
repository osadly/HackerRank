m1,m2=[],[]

for i in range(3):
    x=input().rstrip().split()
    y=list(map(int,x))
    m1.append(y)

for i in range(3):
    x=input().rstrip().split()
    y=list(map(int,x))
    m2.append(y)

for i in range(3):
    for j in range(3):
        print(m1[i][j]-m2[i][j])
        #return m1[i][j]-m2[i][j]
