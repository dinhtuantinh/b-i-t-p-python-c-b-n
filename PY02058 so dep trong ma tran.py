a=[int(i) for i in input().split()]
n=a[0];m=a[1]
arr=[]
for i in range(n):
    arr.append([int(j) for j in input().split()])
Max=arr[0][0];Min=Max
for i in range(n):
    for j in range(m):
        if arr[i][j]>Max:
            Max=arr[i][j]
        if arr[i][j]<Min:
            Min=arr[i][j]
res=Max-Min
check=0
for i in range(n):
    for j in range(m):
        if arr[i][j]==res:
            check=1
            break
if check==0:print("NOT FOUND")
else:
    print(res)
    for i in range(n):
        for j in range(m):
            if arr[i][j]==res:
                print("Vi tri [",end="")
                print(i,end="][")
                print(j,end="]")
                print()