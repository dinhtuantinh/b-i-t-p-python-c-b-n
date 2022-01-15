t=int(input())
for k in range(t):
    n=int(input())
    a=[int(i) for i in input().split()]
    dem=0
    for i in range(n-1):
        tmp=0
        for j in range(i+1,n):
            if a[i]>a[j] and tmp>dem:
                dem=tmp
            