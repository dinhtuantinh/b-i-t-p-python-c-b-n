import math
def CheckNT(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return n>1
def USCLN(a, b):
    if b == 0:
        return a
    return USCLN(b, a % b)
def sum_chu_so(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
t=int(input())
for test in range(t):
    arr=[int(i) for i in input().split()]
    a=arr[0]
    b=arr[1]
    c=USCLN(a, b)
    k=sum_chu_so(c)
    if CheckNT(k):
        print("YES")
    else:
        print("NO")
