import numpy as np 
n,m=(int(i) for i in input().split())
a=[[int(i) for i in input().split()] for i in range(n)]
k,t=(int(i) for i in input().split())
b=[]
for i in range(m):
    if i==k:
        b.append(t)
    elif i==t:
        b.append(k)
    else:
        b.append(i)
arr = np.array(a)
i = np.argsort(b)
arr=arr[:,i]
for i in range(n):
    for j in range(m):
        print(arr[i][j],end=' ')
    print()
