if __name__ == '__main__':
    s = input()
    bIsalnum,bIsalpha,bIsdigit,bIslower,bIsUpper = False, False,False, False,False
    for e in s:
        bIsalnum = bIsalnum or e.isalnum()
        bIsalpha = bIsalpha or e.isalpha()
        bIsdigit = bIsdigit or e.isdigit()
        bIslower = bIslower or e.islower()
        bIsUpper = bIsUpper or e.isupper()
        
    print(bIsalnum)
    print(bIsalpha)
    print(bIsdigit)
    print(bIslower)
    print(bIsUpper)
     