import math
n=int(input())
a=[]
hang=[0]*n
cot=[0]*n
count=0
for i in range(n):
    tmp=input()
    for j in range(len(tmp)):
        if tmp[j]=='C':
            hang[i]+=1
            cot[j]+=1
for i in hang:
    if i>=2:
        count+=math.comb(i,2)
for i in cot:
    if i>=2:
        count+=math.comb(i,2)
print(count)
