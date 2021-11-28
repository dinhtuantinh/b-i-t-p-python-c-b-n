n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append([int(j) for j in input().split()])
max=0
for i in range(n):
    for j in range(m):
        if a[i][j]>max:
            max=a[i][j]
min=max
for i in range(n):
    for j in range(m):
        if a[i][j]<min:
            min=a[i][j]
res=max-min
mm=0
for i in range(n):
    for j in range(m):
        if a[i][j]==res:
            mm=1
            break
if mm==1:
    print(res)
    for i in range(n):
        for j in range(m):
            if a[i][j]==res:
                print("Vi tri [",end='')
                print(i,end=']')
                print('[',end='')
                print(j,end=']')
                print()
else:
    print("NOT FOUND")

