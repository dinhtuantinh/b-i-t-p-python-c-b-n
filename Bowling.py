n,k=(int(i) for i in input().split())
a=[]
b=[]
for i in range(k):
    p,q=(int(i) for i in input().split())
    a.append(p-1)
    b.append(q-1)
count=dict()
for i in range(k):
    for i in range(a[i],b[i]+1):
        count[i]=0
for i in range(n):
    if not(i in count):
        print("I",end='')
    else:
        print(".",end='')