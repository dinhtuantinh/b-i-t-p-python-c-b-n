def prime(n):
    count = 0
    for i in range(1,n+1):
        if n%i==0: count+=1
    if count==2:return 1
    return 0
a=[]
n,m=map(int,input().split())
for i in range(n):
    a.append([int(j) for j in input().split()])
for i in range(n):
    for j in range(m):
        print(prime(a[i][j])," ",end='')
    print("\n")
