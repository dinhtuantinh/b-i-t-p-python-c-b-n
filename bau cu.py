n,k=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
d=dict()
for i in a:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
max1=0
for key in list(d.keys()):
    if d[key]>max1:
        max1=d[key]
min1=0
for key in list(d.keys()):
    if d[key]==max1:
        continue
    else:
        if min1<d[key]:
            min1=d[key]
if min1==0:
    print("NONE")
else:
    check=0
    for key in list(d.keys()):
        if d[key]==min1:
            print(key)
            check=1
            break
    if check==0:
        print("NONE")
