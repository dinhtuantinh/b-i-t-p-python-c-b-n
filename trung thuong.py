def initwsolve():
    f={}
    n=int(input())
    for i in range(n):
        x=int(input())
        if x in f:
            f[x]+=1
        else:
            f[x]=1
    res=1e9;max=1
    for i in f:
        if f[i]>max: max=f[i]
    for i in f:
        if f[i]==max: res=min(res,int(i))
    print(res)
for i in range (int(input())):
    initwsolve()
