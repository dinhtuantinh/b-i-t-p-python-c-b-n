a=[int(x) for x in input().split()]
d=dict()
for i in a:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
for key in list(d.keys()):
    if d[key]==1:
        print(key,end=' ')