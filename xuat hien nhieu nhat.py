t = int(input())
for test in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    d=dict()
    for i in a:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    max1=n//2
    res1=0
    for key in list(d.keys()):
        if(d[key]>max1):
            max1=d[key]
            res1=key
        elif d[key]==max1:
            continue
    if res1==0:
        print("NO")
    else:
        print(res1)
