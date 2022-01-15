t=int(input())
for k in range(t):
    n=int(input())
    a=[int(i) for i in input().split()]
    d=dict()
    for i in a:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    dem=0
    for key in list(d.keys()):
         if(d[key]>1):
             dem+=d[key]-1
    L=min(a)
    R=max(a)
    print(R-L-n+dem+1)