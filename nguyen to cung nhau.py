def USCLN(a, b):
    if b == 0:
        return a
    return USCLN(b, a % b)
n = int(input())
a = [int(i) for i in input().split()]
a.sort()
for i in range(n-1):
    for j in range(i+1,n,1):
        if USCLN(a[i], a[j])==1:
            print(a[i], a[j])
