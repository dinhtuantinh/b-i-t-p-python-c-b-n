import math
def TN(n):
    s=str(n)
    if s==s[::-1] and len(s)>1: return True
    else: return False
a=[int(i) for i in input().split()]
n=a[0];m=a[1]
arr=[]
for i in range(n):
    arr.append([int(j) for j in input().split()])
Max=0;check=0
for i in range(n):
    for j in range(m):
        if TN(arr[i][j]):
            Max=arr[i][j]
            check=1
            break
if check==0:print("NOT FOUND")
else:
    for i in range(n):
        for j in range(m):
            if TN(arr[i][j]) and arr[i][j]>Max:
                Max=arr[i][j]
    print(Max)
    for i in range(n):
        for j in range(m):
            if arr[i][j]==Max:
                print("Vi tri [",end="")
                print(i,end="][")
                print(j,end="]")
                print()