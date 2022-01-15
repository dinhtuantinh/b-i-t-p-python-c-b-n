def NTCN(a,b):
    if b==0:
       return a==1
    return NTCN(b,a%b)
n=int(input())
a = [int(i) for i in input().split()]
a.sort()
for i in range(n-1):
    for j in range(i+1,n):
        if NTCN(a[i],a[j])==1:
            print(a[i],end=" ")
            print(a[j])