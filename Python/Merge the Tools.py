def merge_the_tools(string, k):
    n = len(string)
    x=n//k
    
    arStr=[]
    for i in range(0,n,k):
        arStr.append(string[i:i+k])
        #print(string[i:i+k])
        
    chrLst=[0]*26
        
    for es in arStr:
        tmp=""
        chrLst=[0]*26
        for ec in es:
            if chrLst[ord(ec)-ord('A')] == 0:
                tmp+=ec
                chrLst[ord(ec)-ord('A')]+=1
                
        print(tmp)
    
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)