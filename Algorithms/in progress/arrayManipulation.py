def arrayManipulation(n, queries):
    lst=[0]*n
    m=len(queries)
    for i in range(m):
        a=queries[i][0]
        b=queries[i][1]
        k=queries[i][2]
        lst1=lst[a-1:b]
        lst1=list(map(lambda x:x+k,lst1))
        lst[a-1:b]=lst1
        
    return max(lst)