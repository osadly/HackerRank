def ListComprehensions(x,y,z,n):
    A = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n:
                    A.append([i,j,k])
                    
    return A
    
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print(ListComprehensions(x,y,z,n))
