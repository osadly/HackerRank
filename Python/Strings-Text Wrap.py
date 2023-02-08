import textwrap

def wrap(string, max_width):
    #ret=[]
    ret=""
    while string is not None and len(string)>0:
        tmp=string[:max_width]
        #ret.append(tmp)
        ret +=tmp + "\n"
        
        if tmp=="" or tmp is None:
            return
        
        #print(string,tmp)
        string=string[max_width:]
        
    return ret

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)