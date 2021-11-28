import decimal
n=int(input())
a = [float(i) for i in input().split()]
a.sort()
min=a[0];max=a[n-1]
b=[]
for i in range(n):
    if a[i]!=min and a[i]!=max:
        b.append(a[i])
d=dict()
for i in b:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
sum=0
dem=0
for key in list(d.keys()):
    sum+=d[key]*key
    dem+=d[key]
print(round((sum/dem),2))
