import math

def solve(a, b, n):
    cnstFrMdl = int(1e+9 + 7)
    #print(cnstFrMdl)
    # any term Tn will be calculated as shown below
    # Tn = F_N * b + F_N-1 * a
    # where F_N,F_N-1 is the n & n-1 fib terms in the fib series
    # step 1 calc F_N
    # step 2 calc F_N-1
    # step 3 calc F_N * b + F_N-1 * a - return this result
    # all above steps followed and it is working fie for small numbers but solution yet to be
    # updated to be used for large numbers (see NEXT STEP below)

    sqrt5 = math.sqrt(5)
    #print("sqrt5=",sqrt5)
    OneOverSqrt5 = 1 / math.sqrt(5)
    #print("OneOverSqrt5=",OneOverSqrt5)
    sqrt5Plus1Over2 = (1 + sqrt5) / 2
    #print("sqrt5Plus1Over2=",sqrt5Plus1Over2)
    sqrt5Minus1Over2 = (1 - sqrt5) / 2
    #print("sqrt5Minus1Over2=",sqrt5Minus1Over2)

    # NEXT STEP: is to design/update below lines to use pow function in python along with "cnstFrMdl" to have the number within limits
    F_N = OneOverSqrt5 * (math.pow(sqrt5Plus1Over2, n) - math.pow(sqrt5Minus1Over2, n))
    # below lines not working as pow parameters should be integers - SO below line gives compile error as first parameter should be integer
    #F_N = OneOverSqrt5 * ( pow(sqrt5Plus1Over2, n,cnstFrMdl) - pow(sqrt5Minus1Over2, n, cnstFrMdl) )
    print(F_N)
    #return 1

    F_N_1 = OneOverSqrt5 * ( math.pow(sqrt5Plus1Over2,n-1) - math.pow(sqrt5Minus1Over2,n-1) )
    print(F_N_1)
    Trm1 = int(round(b * F_N) % cnstFrMdl)
    #print(Trm1)
    Trm2 = int(round(a * F_N_1) % cnstFrMdl)
    #print(Trm2)
    CustFib_N = Trm1 + Trm2
    #print(CustFib_N)
    #CustFib_N = math.fmod()
    return int(round(CustFib_N))

print(solve(9000,8000,1000))
#print(solve(9000,8000,3000))
print(solve(2,4,9  ))
#print(solve(1,7,2  ))
#print(solve(1,8,1  ))
#print(solve(4,3,1  ))
#print(solve(3,7,5 ))