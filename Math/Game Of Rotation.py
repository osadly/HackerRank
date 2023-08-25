first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

arr = input().rstrip().split()
arr=list(map(lambda x:int(x), arr))

#print(n,arr)
PMEAN=[0]*n
for i in range(n):
    PMEAN[0]+=arr[i]*(i+1)

sm=sum(arr)
for i in range(1,n):
    PMEAN[i]=PMEAN[i-1]-sm+n*arr[i-1]
    
print(max(PMEAN))