m,n=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]
a=set(a)
b=set(b)
a,b=sorted(a),sorted(b)
for i in a:
    if i in b:
        print(i,end=' ')
print()
for i in a:
    if i not in b:
        print(i,end=' ')
print()
for i in b:
    if i not in a:
        print(i,end=' ')
