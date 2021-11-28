t=int(input())
for test in range(t):
    s=str(input())
    n=str(input())
    k=len(n)
    dem=0
    res=0
    count=0
    i=0
    while(i<len(s)):
        res=res*10+(int)(s[i])
        dem+=1
        if dem==k:
            if str(res)==n:
                count+=1
                res=0
                i+=k
                dem=0
            else:
                i-=k+2
                res=0
                dem=0
        elif dem<k:
            i+=1
    print(count)