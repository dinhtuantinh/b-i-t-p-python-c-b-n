m,n=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
a=set(a)
b=set(b)
a,b=sorted(a),sorted(b)
check=1
for i in a:
    if i not in b:
        check=0
        break
if check==1:
    print("YES")
else:
    print("NO")
