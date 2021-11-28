import math
n=int(input())
a=[]
for i in range(n):
    a.append([int(j) for j in input().split()])
k=int(input())
stren=0;sduoi=0
for i in range(0,n-1):
    for j in range(0,n-i-1):
        stren+=a[i][j]
for i in range(1,n):
    for j in range(n-i,n):
        sduoi+=a[i][j]
res=abs(stren-sduoi)
if res>k:
    print("NO")
    print(res)
else:
    print("YES")
    print(res)
