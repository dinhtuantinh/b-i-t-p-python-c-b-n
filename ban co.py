import numpy as np
n,m=(int(x) for x in input().split())
a=np.random.rand(n,m)
for i in range(n):
    for j in range(n):
        if (i+j)%2==0:
            print('.',end=' ')
        else:
            print('*',end=' ')
    print()