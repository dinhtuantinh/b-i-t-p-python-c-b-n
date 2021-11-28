T=int(input())
for t in range (T):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    a.sort()
    b.sort()
    dem=0
    for i in range(n):
        if(a[i]>b[i]):
            print("NO")
            dem+=1
            break
    if(dem == 0):
        print("YES")
