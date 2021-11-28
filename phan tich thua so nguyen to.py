import math
t = int(input())
for test in range(t):
    n=int(input())
    print(1,end='')
    k=int(math.sqrt(n))
    for i in range(2,k,1):
        if n%i==0:
            dem=0
            print(' *',i,end='')
            print('^',end='')
            while(n%i==0):
                dem+=1
                n/=i
            print(dem,end='')
    n=int(n)
    if n>1:
        print(' *',(n),end='')
        print('^',end='')
        print(1)
    else:
        print()
