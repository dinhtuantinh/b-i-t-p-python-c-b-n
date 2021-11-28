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
t=int(input())
for test in range(t):
    n=int(input())
    k=0
    for i in range(n):
        if USCLN(i,n)==1:
            k+=1
    if CheckNT(k):
        print("YES")
    else:
        print("NO")
