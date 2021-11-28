import math
def CheckNT(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return n>1
n=int(input())
a=[int(i) for i in input().split()]
b=[]
for i in range(n):
    if CheckNT(a[i]):
        b.append(a[i])
b.sort()
j=0
for i in range(n):
    if CheckNT(a[i]):
        print(b[j],end= ' ')
        j+=1
    else:
        print(a[i],end=' ')
