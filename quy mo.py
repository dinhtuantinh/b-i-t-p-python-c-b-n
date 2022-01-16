import numpy as np 
n,m=(int(i) for i in input().split())
a=[[int(i) for i in input().split()] for i in range(n)]
k=int(input())
arr = np.array(a)
arr=arr*k
for i in range(n):
    for j in range(m):
        print(arr[i][j],end=' ')
    print()