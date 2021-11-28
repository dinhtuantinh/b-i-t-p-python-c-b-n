import math
def CheckNT(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return n>1

m,n = list(map(int,input().split()))
#arr = ((int(x) for x in input().split())for i in range(m))
a=[]
for i in range(m):
    arr=[]
    for j in range(n):
        #arr = ((int(x) for x in input().split())for i in range(n))
        x = int(input())
        #print(end=' ')
        arr.append(x)
    a.append(arr)
for i in range(0, m):
    for j in range(0, n):
        if CheckNT(a[i][j]):
            a[i][j]=1
        else:
            a[i][j]=0
for i in range(0, m):
    for j in range(0, n):
        print(a[i][j], end=' ')
    print()
