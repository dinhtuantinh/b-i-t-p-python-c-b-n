a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
c=list(set(a)&set(b))
c.sort()
print(*c)