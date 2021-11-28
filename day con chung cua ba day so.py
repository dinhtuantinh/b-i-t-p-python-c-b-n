t=int(input())
for test in range(t):
    n,m,q=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    c=[int(x) for x in input().split()]
    i,j,k,check=0,0,0,0
    while i<n and j<m and k<q:
        if a[i]==b[j] and b[j]==c[k]:
            print(a[i],end=' ')
            check=1
            i+=1
            j+=1
            k+=1
        elif a[i]<b[j]:
            i+=1
        elif b[j]<c[k]:
            j+=1
        else:
            k+=1
    if check==0:
        print("NO")
    print()
