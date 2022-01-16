a=input()
a=a.split()
c=dict()
for i in a:
    if not(i in c):
        print("NO")
        c[i]=0
    else:
        print("YES")