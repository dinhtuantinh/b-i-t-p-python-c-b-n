#[str(j) for j in input().split()]
import math
n=int(input())
a=[]
for i in range(n):
    for j in range(n):
        s=str(input())
        if s=='C':
            a.append(1)
        else: a.append(0)
s=0
for k in range(n):
    count=0
    for z in range(n):
        if a[k][z]==1:
            count+=1
    s+=(count*(count-1))/2
for x in range(n):
    count=0
    for y in range(n):
        if a[y][x]==1:
            count+=1
    s+=(count*(count-1))/2
print(s)