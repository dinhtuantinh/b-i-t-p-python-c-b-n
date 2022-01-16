import numpy as np
n=int(input())
a=np.random.rand(n,n)
for i in range(n):
    for j in range(n):
        a[i][j]=abs(i-j)
for i in range(n):
    for j in range(n):
        print(int(a[i][j]),end=' ')
    print()