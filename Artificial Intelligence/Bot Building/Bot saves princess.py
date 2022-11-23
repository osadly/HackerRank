#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    #print("hi")
    mapDict = { 'D': 'DOWN', 'U': 'UP', 'L': 'LEFT','R': 'RIGHT'}
    #print all the moves here
    drct=""
    d=int((n-1)/2)
    if(grid[0][0]=='p'):
        drct='L'*d + 'U'*d
    elif(grid[n-1][0]=='p'):
        drct='L'*d + 'D'*d
    elif(grid[n-1][n-1]=='p'):
        drct='R'*d + 'D'*d
    elif(grid[0][n-1]=='p'):
        drct='R'*d + 'U'*d
    
    sMoves=""
    for e in drct:
        sMoves += mapDict[e]
        sMoves += "\n"
        
    print(sMoves)
    #return sMoves
    
    #for i in len()

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
