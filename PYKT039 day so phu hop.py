t=int(input())
for k in range(t):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    a.sort()
    b.sort()
    check=0
    for i in range(n):
        if a[i]>b[i]:
            check=1
            print("NO")
            break
    if check==0:print("YES")
    