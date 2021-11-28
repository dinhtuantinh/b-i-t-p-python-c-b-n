a=[]
n,m=map(int,input().split())
for i in range(n):
    a.append([int(j) for j in input().split()])
if n>m:
    for i in range(n):
        check=0
        for j in range(m):
            if i<m:
                if i%2!=0:
                    print(a[i][j], end=' ')
                    check=1
            else:
                print(a[i][j],end=' ')
                check=1
        if check==1: print()
elif n<m:
    for i in range(n):
        check=0
        for j in range(m):
            if j<n:
                if j%2==0:    
                    print(a[i][j], end=' ')
                    check=1
            else:
                print(a[i][j],end=' ')
                check=1
        if check==1: print()
else:
    for i in range(n):
        for j in range(m):
            print(a[i][j],end=' ')
        print()