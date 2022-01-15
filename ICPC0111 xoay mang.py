t=int(input())
for k in range(t):
    m=[int(i) for i in input().split()]
    n=m[0]
    d=m[1]
    a=[int(i) for i in input().split()]
    for i in range(d,n):
        print(a[i],end=" ")
    for i in range(0,d):
        print(a[i],end=" ")
    print()