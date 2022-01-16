import numpy as np 
n,m=(int(i) for i in input().split())
bb=[[int(i) for i in input().split()] for i in range(n)]
arr = np.array(bb)
k=arr.max()
check=False
for i in range(n):
    for j in range(m):
        if(arr[i][j]==k):
            print(f'{i} {j}')
            check=True
            break
    if check==True:
        break