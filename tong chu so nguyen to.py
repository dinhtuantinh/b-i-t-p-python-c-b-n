import math
def CheckNT(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i ==0:
            return False
    return n>1
t=int(input())
for test in range(t):
    s=str(input())
    sum=0
    for i in range(len(s)):
        sum+=int(s[i])
    if CheckNT(sum):
        print("YES")
    else:
        print("NO")
