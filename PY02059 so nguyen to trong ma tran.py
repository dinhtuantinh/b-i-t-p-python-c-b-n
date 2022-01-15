import math
def CheckNT(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return n>1
a=[int(i) for i in input().split()]
n=a[0];m=a[1]
arr=[]
for i in range(n):
    arr.append([int(j) for j in input().split()])
Max=0;check=0
for i in range(n):
    for j in range(m):
        if CheckNT(arr[i][j]):
            Max=arr[i][j]
            check=1
            break
if check==0:print("NOT FOUND")
else:
    for i in range(n):
        for j in range(m):
            if CheckNT(arr[i][j]) and arr[i][j]>Max:
                Max=arr[i][j]
    print(Max)
    for i in range(n):
        for j in range(m):
            if arr[i][j]==Max:
                print("Vi tri [",end="")
                print(i,end="][")
                print(j,end="]")
                print()