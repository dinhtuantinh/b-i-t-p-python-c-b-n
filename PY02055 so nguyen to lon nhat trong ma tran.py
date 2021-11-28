import math
def CheckNT(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return n>1
n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append([int(j) for j in input().split()])
nt=0
for i in range(n):
    for j in range(m):
        if CheckNT(a[i][j])==1 and a[i][j]>nt:
            nt=a[i][j]
if nt==0:
    print("NOT FOUND")
else:
    print(nt)
    for i in range(n):
        for j in range(m):
            if a[i][j]==nt:
                print("Vi tri [",end='')
                print(i,end=']')
                print('[',end='')
                print(j,end=']')
                print()