def slove():
    n,p=[int(i) for i in input().split()]
    res=0
    x=1
    while n/(p**x)>1:
        res+=int(n/(p**x))
        x+=1
    print(res)
t=int(input())
for i in range(t):
    slove()
