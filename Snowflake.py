import numpy as np
# n,m=(int(x) for x in input().split())
n=int(input())
a=np.random.rand(n,n)
for i in range(n):
    for j in range(n):
        if i==j:
            print('*',end=' ')
        elif i+j==n-1:
            print('*',end=' ')
        elif i==n//2 or j==n//2:
            print('*',end=' ')
        else:
           print('.',end=' ') 
    print()