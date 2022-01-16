import numpy as np
# n,m=(int(x) for x in input().split())
n=int(input())
a=np.random.rand(n,n)
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print('1',end=' ')
        elif i+j>n-1:
            print('2',end=' ')
        else:
           print('0',end=' ') 
    print()